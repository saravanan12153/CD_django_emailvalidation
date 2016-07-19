from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Email
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
    return render(request, 'emailapps/index.html')

def process(request):
    if Email.emailManager.isValidEmail(request.POST['email']):
        Email.emailManager.create(email=request.POST['email'])
        messages.success(request, 'The email address you entered ' + request.POST['email']+ ' is a VALID email address! Thank you!')
        return redirect (reverse('success'))
    else:
        messages.warning(request, 'Invalid email!')
        return redirect (reverse('index'))

def success(request):
    context = {
        "emails": Email.emailManager.all()
    }
    return render(request, 'emailapps/success.html', context)
