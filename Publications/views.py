from django.shortcuts import render, HttpResponse
from datetime import datetime
from Publications.models import Contact, Published
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def publications(request):
    jour_paper = Published.objects.filter(type="JOUR")
    conf_paper = Published.objects.filter(type="CONF")
    other = Published.objects.filter(type="OTHR")
    params = {'journal': jour_paper, 'conference': conf_paper, 'others': other}
    return render(request, 'publications.html', params)

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!') 
 
    return render(request, 'contact.html')