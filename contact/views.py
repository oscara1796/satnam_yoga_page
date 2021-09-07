from django.shortcuts import render, redirect
from django.urls import reverse
from contact.forms import ContactForm
from django.conf import settings
from django.core.mail import EmailMessage

# Create your views here.


def contact(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data= request.POST)
        if contact_form.is_valid():
            name=request.POST.get('name')
            email=request.POST.get('email')
            content=request.POST.get('content')

            email= EmailMessage(
            f'Nuevo  de la Página Sat Nam de {name}',
            f"De {name} <{email}> \n\nEscibió:\n\n{content}",
            settings.DEFAULT_FROM_EMAIL,
            ['oscara1706cl@gmail.com', settings.DEFAULT_FROM_EMAIL]
            )
            try:
                email.send(fail_silently=False)
                return redirect(reverse('contact')+'?ok')
            except:
                return redirect(reverse('contact')+'?fail')


    return render(request,'contact/contact.html',{'form':contact_form})
