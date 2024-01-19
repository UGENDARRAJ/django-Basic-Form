from django.shortcuts import render, redirect
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
        return redirect('home')
    return render(request,'home.html')

def updateData(request, id):
    mydata=Datas.objects.get(id=id)
    return render(request, 'update.html', {'data':mydata})