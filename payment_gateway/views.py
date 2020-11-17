from django.shortcuts import render 

# Create your views here.

def home(request):
    return render(request,'payment_gateway/home.html')

def detail(request):
    return render(request,'payment_gateway/detail.html')


def about(request):
    return render(request,'payment_gateway/about.html')

def detail(request):
    return render(request,'payment_gateway/detail.html')

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

def payment(request):
    if request.method == 'POST':
        email = request.POST['inputemail']
        name = request.POST['inputname']
        amount = request.POST['amt']

        template = render_to_string('payment_gateway/email_templates.html',{'name':name,'amount':amount})


        email = EmailMessage(
            'THANK YOU FOR YOUR DOANTION!!',
            template,
            settings.EMAIL_HOST_USER,
            [email],   
        )
        #email.fail.silently = False
        email.send()
         


        
    return render(request,'payment_gateway/payment.html')