import stripe
from datetime import datetime
from django.shortcuts import render, redirect
from django.conf import settings
from django.http.response import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.utils import timezone, dateformat
from users.models import Profile, statusChoices
from django.views.decorators.http import require_POST
from paypalrestsdk.notifications import WebhookEvent
from .models import Paypal
import paypalrestsdk
import json
import requests
import base64
import pytz
# Create your views here.



def get_paypal_token():
    """
    Obtenemos el token de paypal de nuestra cuenta
    """
    credentials = "%s:%s" % (settings.PAYPAL_CLIENT_ID, settings.PAYPAL_SECRET_ID)
    encode_credential = base64.b64encode(credentials.encode('utf-8')).decode('utf-8').replace("\n", "")
    headers = {
    "Authorization": ("Basic %s" % encode_credential),
    'Accept': 'application/json',
    'Accept-Language': 'en_US',
    }
    param = {
    'grant_type': 'client_credentials',
    }
    r = requests.post(settings.URL_PAYPAL_TOKEN, headers=headers, data=param).json()
    return  r['access_token']

def paypal_handle(request):
    """
    Manejamos las peticiones POST cuando se sube el formulario de paypal_form y añadimos el profile
    OBJ request
    """
    if request.method == 'POST':
        # print(request.POST)
        user = request.user
        session = request.POST.get('details')
        session = json.loads(session)
        # print('session: ', str(session))
        profile_exists= Profile.objects.filter(user=user).exists()
        if not profile_exists:
            # print(session['subscriptionID'])
            # print(session['plan_id'])
            Profile.objects.create(
                user=user,
                paypalSubscriptionId= session['subscriptionID'],
                paypalPlanId= session['plan_id'],
                active= statusChoices.ACTIVE,
            )
            return True
        # else:
        #     profile= Profile.objects.get(user=user)
        #     profile.paypalSubscriptionId = stripe_subscription_id
        #     profile.active = True
        #     profile.save()
    return False

def HomePagePaymentView(request):
    """
    Manejamos la API  de stripe mostrando opciones de pago,  la subscripción que tiene el ususario subscrito y llevandolos
    a la pasarela de pago  de stripe ademas de invocar la funcion de paypal por si pagan con paypal y si es con paypal hacemos request a su api
    para traer la un token y traer la info del plan
    OBJ request
    """
    # print(request.user)
    red_value=paypal_handle(request)
    if red_value:
        return redirect('update_profile')
    stripe.api_key = settings.STRIPE_SECRET_KEY
    month_subs= stripe.Product.retrieve(settings.STRIPE_PRODUCT_ID)
    month_subs_price= stripe.Price.retrieve(settings.STRIPE_PRICE_ID)
    year_subs= stripe.Product.retrieve(settings.STRIPE_PRODUCT_YEAR_ID)
    year_subs_price= stripe.Price.retrieve(settings.STRIPE_PRICE_YEAR_ID)
    paypal_plans = Paypal.objects.all()
    try:
        # Retrieve the subscription & product
        customer = Profile.objects.get(user=request.user)
        product = None
        subscription = None
        if customer.stripeSubscriptionId:
            subscription = stripe.Subscription.retrieve(customer.stripeSubscriptionId)
            product = stripe.Product.retrieve(subscription.plan.product)
            if product.id == month_subs.id:
                product['price'] = round(float(month_subs_price.unit_amount /100),2)
                product['type'] = "Subscripción mensual"
            else:
                product['price'] = round(float(year_subs_price.unit_amount /100),2)
                product['type'] = "Subscripción anual"
        elif customer.paypalSubscriptionId and customer.paypalPlanId:
            access_token = get_paypal_token()
            headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {access_token}' }
            url = f'https://api-m.paypal.com/v1/billing/plans/{customer.paypalPlanId}'
            r = requests.get(url, headers=headers).json()
            current_plan = None
            for plan in paypal_plans:
                if plan.paypalPlanId ==  customer.paypalPlanId:
                    current_plan = plan
            subs_price =r['billing_cycles'][0]['pricing_scheme']['fixed_price']

            product= {'name': r['name'], 'price': subs_price['value'], 'type': current_plan.name, 'description': current_plan.description, 'images': [current_plan.image.url]}
            # print(current_plan.image.url)
            url = f'https://api-m.paypal.com/v1/billing/subscriptions/{customer.paypalSubscriptionId}'
            subscription = requests.get(url, headers=headers).json()


        list_products= [product]
        # Feel free to fetch any additional data from 'subscription' or 'product'
        # https://stripe.com/docs/api/subscriptions/object
        # https://stripe.com/docs/api/products/object
        return render(request, 'payments/payment_home.html', {
            'subscription': subscription,
            'list_products':list_products,
            'profile': customer
        })

    except Profile.DoesNotExist :

        product_1= {"id":"but_1","price_id":month_subs_price.id,'name': month_subs.name, 'description': month_subs.description, 'price':round(float(month_subs_price.unit_amount /100),2), 'type': "Subscripción mensual", 'images': month_subs.images}
        product_2= {"id":"but_2","price_id":year_subs_price.id,'name': year_subs.name, 'description': year_subs.description, 'price':round(float(year_subs_price.unit_amount /100),2), 'type': "Subscripción anual" , 'images': year_subs.images}
        list_products= [product_1,product_2]

        return render(request, 'payments/payment_home.html',{'list_products':list_products, 'profile': Profile.DoesNotExist, 'paypal_plans': paypal_plans})


def SuccessPaymentView(request):
    return render(request, 'payments/success.html')

def CancelledPaymentView(request):
    return render(request, 'payments/cancelled.html')

def Cancelled_or_Reactivate_SubscriptionView(request):
    """ Modificamos a periodo de prueba la subscripción  de Stripe o la volvemos a activar si es que estaba en prueba
    Object Request"""
    # Retrieve the subscription & product
    stripe_customer = Profile.objects.get(user=request.user)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    subscription = stripe.Subscription.retrieve(stripe_customer.stripeSubscriptionId)
    if subscription.cancel_at_period_end == True:
        stripe.Subscription.modify(
        stripe_customer.stripeSubscriptionId,
        cancel_at_period_end=False
        )
        stripe_customer.active= statusChoices.ACTIVE
        stripe_customer.save()
        return redirect('feed')
    else:
        stripe.Subscription.modify(
        stripe_customer.stripeSubscriptionId,
        cancel_at_period_end=True
        )
        stripe_customer.active= statusChoices.TRIAL
        stripe_customer.save()
        subscription = stripe.Subscription.retrieve(stripe_customer.stripeSubscriptionId)
        timestamp= datetime.fromtimestamp(subscription.current_period_end)


        return render(request, 'payments/cancelled.html', {
            'subscription': subscription,
            'time_left':timestamp
        })


def suspend_paypal_View(request):

    # Retrieve the subscription & product
    customer = Profile.objects.get(user=request.user)
    access_token = get_paypal_token()

    headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {access_token}' }
    url2 = f'https://api-m.paypal.com/v1/billing/subscriptions/{customer.paypalSubscriptionId}/suspend'
    url = f'https://api-m.paypal.com/v1/billing/subscriptions/{customer.paypalSubscriptionId}'
    subscription = requests.get(url, headers=headers).json()
    date_format = '%Y-%m-%dT%H:%M:%SZ'
    last_payment = subscription["billing_info"]["last_payment"]["time"]
    last_payment= datetime.strptime(last_payment, date_format)
    last_payment = pytz.utc.localize(last_payment)
    # print("THIS IS LAST DATE PAYMENT: ", last_payment)
    paypal_plan = subscription["plan_id"]
    paypal_plans = Paypal.objects.all()
    post_req= requests.post(url2, headers=headers)
    # print("post_request ", post_req )
    customer.active = statusChoices.TRIAL
    for plan in paypal_plans:
        if plan.SKU == 'PLAN_ANUAL':
            customer.paypal_cancel_date= last_payment + timezone.timedelta(days=365)
        elif plan.SKU == 'PLAN_MENSUAL':
            customer.paypal_cancel_date= last_payment + timezone.timedelta(days=30)
    # print("THIS IS update DATE PAYMENT in profile: ", last_payment + timezone.timedelta(days=365))
    customer.save()
    subscription = requests.get(url, headers=headers).json()
    timestamp= customer.paypal_cancel_date


    return render(request, 'payments/cancelled.html', {
        'subscription': subscription,
        'time_left':timestamp
    })

def reactivate_paypal_View(request):

    # Retrieve the subscription & product
    customer = Profile.objects.get(user=request.user)
    access_token = get_paypal_token()

    headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {access_token}' }
    url = f'https://api-m.paypal.com/v1/billing/subscriptions/{customer.paypalSubscriptionId}/activate'

    requests.post(url, headers=headers)
    customer.active = statusChoices.ACTIVE
    customer.paypal_cancel_date= None
    customer.save()
    timestamp= customer.paypal_cancel_date

    url = f'https://api-m.paypal.com/v1/billing/subscriptions/{customer.paypalSubscriptionId}'
    subscription = requests.get(url, headers=headers).json()

    return redirect('payment_home')



@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=request.user.id if request.user.is_authenticated else None,
                success_url=domain_url + 'payments/success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'payments/cancelled/',
                payment_method_types=['card'],
                mode='subscription',
                line_items=[
                    {
                        'price': settings.STRIPE_PRICE_ID,
                        'quantity': 1,
                    }
                ]
            )

            checkout_session_2 = stripe.checkout.Session.create(
                client_reference_id=request.user.id if request.user.is_authenticated else None,
                success_url=domain_url + 'payments/success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'payments/cancelled/',
                payment_method_types=['card'],
                mode='subscription',
                line_items=[
                    {
                        'price': settings.STRIPE_PRICE_YEAR_ID,
                        'quantity': 1,
                    }
                ]
            )
            checkout_session=stripe.checkout.Session.retrieve(checkout_session['id'], expand=['line_items'])
            checkout_session_2=stripe.checkout.Session.retrieve(checkout_session_2['id'], expand=['line_items'])
            print(checkout_session)
            return JsonResponse({'session_subs_Id': checkout_session, 'session_year_Id': checkout_session_2})
            # return JsonResponse({'session': checkout_session})
        except Exception as e:
            return JsonResponse({'error': str(e)})


@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        # print(session)

        # Fetch all the required data from session
        client_reference_id = session.get('client_reference_id')
        user = User.objects.get(id=client_reference_id)
        stripe_customer_id = session.get('customer')
        stripe_subscription_id = session.get('subscription')

        # Get the user and create a new Profile

        profile_exists= Profile.objects.filter(user=user).exists()
        if not profile_exists:
            Profile.objects.create(
                user=user,
                stripeCustomerId=stripe_customer_id,
                stripeSubscriptionId=stripe_subscription_id,
                active= statusChoices.ACTIVE ,
            )
        else:
            profile= Profile.objects.get(user=user)
            profile.stripeSubscriptionId = stripe_subscription_id
            profile.active = statusChoices.ACTIVE
            profile.save()

        profile= Profile.objects.get(user=user)
        stripe.Customer.modify(
        stripe_customer_id,
        name=user.username,
        email=user.email,
        metadata={"user_id": user.id, "profile_id": profile.id }
        )


        print(user.username + ' just subscribed.')
    # if event['type'] == 'customer.subscription.updated':
    #     session = event['data']['object']
    #     stripe_customer_id = session.get('customer')
    #     profile_exists= Profile.objects.filter(stripeCustomerId=stripe_customer_id).exists()
    #     if profile_exists:
    #         profile= Profile.objects.get(stripeCustomerId=stripe_customer_id)
    #         profile.active = statusChoices.CANCELLED
    #         profile.save()
    #         print('CUSTOMER: ', profile)
    #         print('profile.active ', profile.active)

    if event['type'] == 'customer.subscription.deleted':
        session = event['data']['object']
        # print('CUSTOMER CANCELLED: ')
        # print(session)

        stripe_customer_id = session.get('customer')
        profile_exists= Profile.objects.filter(stripeCustomerId=stripe_customer_id).exists()

        if profile_exists:
            profile= Profile.objects.get(stripeCustomerId=stripe_customer_id)
            profile.active = statusChoices.CANCELLED
            profile.save()
            print(profile.active)
            print('CUSTOMER CANCELLED STRIPE: ', profile)
            profile.delete();

    return HttpResponse(status=200)


# PAYPAL  event listener
@require_POST
@csrf_exempt
def webhook_paypal(request):
    print('WEBHOOK WORK')
    print(request.headers)
    transmission_id= request.headers['Paypal-Transmission-Id']
    timestamp= request.headers['Paypal-Transmission-Time']
    webhook_id= settings.PAYPAL_WEEBHOOK_ID
    event_body= request.body.decode('utf-8')
    cert_url = request.headers['Paypal-Cert-Url']
    auth_algo = request.headers['Paypal-Auth-Algo']
    actual_signature = request.headers['Paypal-Transmission-Sig']
    response = WebhookEvent.verify(transmission_id, timestamp, webhook_id, event_body, cert_url, actual_signature, auth_algo)
    print(response)
    if response:
        print('RESPONSE WORKS')
        obj = json.loads(request.body)
        event_type = obj.get('event_type')
        resource= obj.get('resource')

        if event_type == 'PAYMENT.SALE.COMPLETED':
            pass
            # print(resource)
            # subs_id_paypal = resource['billing_agreement_id']
            # print('Se pago una suscripción al final y funciona esta madre')
        if event_type == 'BILLING.SUBSCRIPTION.SUSPENDED':
            # print(resource)
            subs_id_paypal = resource['id']
            profiles = Profile.objects.filter(paypalSubscriptionId=subs_id_paypal)
            profile = profiles[0]
            if profile.paypal_cancel_date== None:
                profile.paypal_cancel_date = timezone.now() - timezone.timedelta(days=2)
                profile.active = statusChoices.TRIAL
                profile.save()
                # print('su date es none ')
            # print('PROFILE: ', profile)
            # print('Subscripción suspendida ')
        if event_type == 'BILLING.SUBSCRIPTION.ACTIVATED':
            pass
            # print(resource)
            # print('Subscripción activada ')
    return HttpResponse(status=200)
