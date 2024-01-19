from django.shortcuts import render
from django.http import HttpResponse
from .models import Datas
# Create your views here.
def home(request):
    mydata=Datas.objects.all()
    if(mydata!=''):
        return render(request,'home.html', {'datas':mydata})
    else:
        return render(request,'home.html')

def addData(request): 
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        contact=request.POST['contact']
        email=request.POST['email']

        obj=Datas()
        obj.Name=name
        obj.Age=age
        obj.Address=address
        obj.Contact=contact
        obj.Email=email
        obj.save()
        mydata = Datas.objects.all()
        return render(request,'home.html',{'datas':mydata})
    return render(request,'home.html')

def updateData(request):
    
    return render(request, 'update.html')