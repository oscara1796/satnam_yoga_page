import requests
import json
import stripe
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from videos.models import Video, Category
from users.models import Profile
from payments.views import get_paypal_token

#Video cipher vdocipher


# Create your views here.

def list_menu(request):
    user= request.user
    stripe.api_key = settings.STRIPE_SECRET_KEY
    month_subs_price= stripe.Price.retrieve(settings.STRIPE_PRICE_ID)
    firts_video =  None
    category= None
    try:
        firts_video =  Video.objects.filter(free_seen= True).first()
        category= firts_video.categories.first()
    except:
        pass

    return render(request, 'videos/feed.html', {'price_subs_month': "{0:.2f}".format(round(float(month_subs_price.unit_amount /100),3)), "firts_video": firts_video, "category": category,"user": user})


def categories_list(request):

    categories_content = Category.objects.all()
    # print(categories_content)

    return render(request, 'videos/videos.html', {'categories_content': categories_content})


def category(request, category_id ):
    categories_content = Category.objects.all()
    category= get_object_or_404(Category,id= category_id)
    video_content = Video.objects.filter(categories=category).order_by('created')
    subscription= None
    try:
        customer = Profile.objects.get(user=request.user)
        if customer.paypalSubscriptionId:
            access_token = get_paypal_token()
            headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {access_token}' }
            url = f'https://api-m.paypal.com/v1/billing/subscriptions/{customer.paypalSubscriptionId}'
            subscription = requests.get(url, headers=headers).json()
            subscription['status'] =  subscription['status'].lower()
        else:
            stripe.api_key = settings.STRIPE_SECRET_KEY
            subscription = stripe.Subscription.retrieve(customer.stripeSubscriptionId)
        return render(request, "videos/videos.html", {"category": category, 'categories_content': categories_content, 'video_content': video_content, 'subscription': subscription})
    except Exception as e:
        return render(request, "videos/videos.html", {"category": category, 'categories_content': categories_content, 'video_content': video_content})




def video_id_show(request, category_id, video_id):
    categories_content = Category.objects.all()
    video= get_object_or_404(Video,id=video_id)
    category= get_object_or_404(Category,id= category_id)
    video_content = Video.objects.filter(categories=category).order_by('created')
    subscription= None
    try:
        customer = Profile.objects.get(user=request.user)
        if customer.paypalSubscriptionId:
            access_token = get_paypal_token()
            headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {access_token}' }
            url = f'https://api-m.paypal.com/v1/billing/subscriptions/{customer.paypalSubscriptionId}'
            subscription = requests.get(url, headers=headers).json()
            subscription['status'] =  subscription['status'].lower()
        else:
            stripe.api_key = settings.STRIPE_SECRET_KEY
            subscription = stripe.Subscription.retrieve(customer.stripeSubscriptionId)

        return render(request, 'videos/videos.html', {
        "category": category,
        'categories_content': categories_content,
        'video_content': video_content,
        'video': video,
        'subscription': subscription
        })
    except Exception as e:
        return render(request, 'videos/videos.html', {
        "category": category,
        'categories_content': categories_content,
        'video_content': video_content,
        'video': video
        })
