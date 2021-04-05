from django.shortcuts import render
from datetime import datetime
from home.models import Contact
# Create your views here.
def ind(request):

    return render(request,'./index.html')

def cups(request):

    return render(request,'./cups.html')

def cons(request):

    return render(request,'./cons.html')

def contact(request):
    # if request.method== 'POST':
    #     name= request.POST.get('name')
    #     email= request.POST.get('email')
    #     desc= request.POST.get('desc')
    #     phone= request.POST.get('phone')
    #     contact = Contact(name=name,email=email,desc=desc,date=datetime.today(),phone=phone)
    #     contact.save()
    return render(request,'contact.html')

def family(request):

    return render(request,'./family.html')

def about(request):

    return render(request,'./about.html')



def contact2(request):
    if request.method== 'POST':
        name= request.POST.get('name')
        email= request.POST.get('email')
        desc= request.POST.get('desc')
        phone= request.POST.get('phone')
        contact = Contact(name=name,email=email,desc=desc,date=datetime.today(),phone=phone)
        contact.save()
    return render(request,'contact2.html')

# def (request):

#     return render(request,'./.html')

