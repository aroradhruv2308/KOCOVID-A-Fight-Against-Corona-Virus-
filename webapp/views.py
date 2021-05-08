from django.shortcuts import render,redirect
import requests
from datetime import datetime
from webapp.models import Contact
from webapp.models import Help
from webapp.models import Plasma
from webapp.models import Oxygen
from webapp.models import Bed
from webapp.models import nHelp


from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact =Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request,'Your message has been sent')

    return render(request,'contact.html')


def help(request):
    if request.method == "POST":
        name = request.POST.get('name')
        city = request.POST.get('city')
        state = request.POST.get('state')
        phone = request.POST.get('phone')
        plasma = request.POST.get('plasma',0)
        oxygen = request.POST.get('oxygen',0)
        bed = request.POST.get('bed',0)
        print(bed)
        print(plasma)
        if plasma == 'on':
            plasma = True
        else:
            plasma = False

        if oxygen == 'on':
            oxygen = True
        else:
            oxygen = False

        if bed == 'on':
            bed = True
        else:
            bed = False
        print(plasma)
        print(bed)
        helpers = Help(name=name,city=city,state=state,phone=phone,oxygen=oxygen,plasma=plasma,bed=bed,date=datetime.today())
        if plasma == True:
            helper1 = Plasma(name = name,city = city,state=state,phone = phone,date=datetime.today())  
            helper1.save()
        if oxygen == True:
            helper2 = Oxygen(name = name,city = city,state=state,phone = phone,date=datetime.today())  
            helper2.save()
        if bed == True:
            helper3 = Bed(name = name,city = city,state=state,phone = phone,date=datetime.today())  
            helper3.save()



        
        helpers.save()
        messages.success(request,'Thanx For Your Contribution')
    return render(request,'help.html')

def nhelp(request):
    if request.method == "POST":
        name = request.POST.get('name')
        city = request.POST.get('city')
        state = request.POST.get('state')
        phone = request.POST.get('phone')
        plasma = request.POST.get('plasma',0)
        oxygen = request.POST.get('oxygen',0)
        bed = request.POST.get('bed',0)
        print(bed)
        print(plasma)
        if plasma == 'on':
            plasma = True
        else:
            plasma = False

        if oxygen == 'on':
            oxygen = True
        else:
            oxygen = False

        if bed == 'on':
            bed = True
        else:
            bed = False
        print(plasma)
        print(bed)
        helpers = nHelp(name=name,city=city,state=state,phone=phone,oxygen=oxygen,plasma=plasma,bed=bed,date=datetime.today())
        helpers.save()
        data1 = None
        data2 = None
        data3 = None
        if helpers.plasma == True:
            data1 = Plasma.objects.all()
        if helpers.oxygen == True:
            data2 = Oxygen.objects.all()
        if helpers.bed == True:
            data3 = Bed.objects.all()

        print(data1)
        print(data2)
        print(data3) 
        context={
        'plasmas':data1,
        'oxygens':data2,
        'beds':data3
        }       
        return render(request,"table.html",context)
        
    return render(request,'nhelp.html')

def table(request):
    
    return render(request,'table.html')







    