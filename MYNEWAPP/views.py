from django.shortcuts import render
from.models import customer
from django.http import HttpResponse
from rest_framework import generics


from .models import StudentData,PlayerDetails,Student5
from .forms import StudentDetails,Student,Cricketplayers
from .serializers import StudentSerializer


# Create your views here.
def firstfunction(request):
    return HttpResponse("<h1>welcome to django</h1>")
def displayform(request):
    form=Student()
    return render(request,'display_form.html',{'form':form})
def formvalidation(request):
    form=StudentDetails()
    if request.method == 'POST':
        form=StudentDetails(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            age=form.cleaned_data['age']
            address=form.cleaned_data['gender']
            gender=form.cleaned_data['gender']
            fruit=form.cleaned_data['favorite_fruit']
            studentdetails=StudentData()
            studentdetails.name=name
            studentdetails.age=age
            studentdetails.address=address
            studentdetails.gender=gender
            studentdetails.favorite_fruit=fruit
            studentdetails.save()
            return HttpResponse("data saved sucessfully")
    return render(request,'display_form.html',{'form':form})
def playerstatics(request):
    form=Cricketplayers()
    if request.method == 'POST':
        form=Cricketplayers(request.POST,request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            age= form.cleaned_data['age']
            address=form.cleaned_data['address']
            role = form.cleaned_data['role']
            COUNTRY= form.cleaned_data['COUNTRY']
            password=form.cleaned_data['password']
            confirmpassword=form.cleaned_data['confirmpassword']
            email=form.cleaned_data['email']
            file=form.cleaned_data['fileupload']
            playerdetails=PlayerDetails()
            playerdetails.name=name
            playerdetails.age=age
            playerdetails.address=address
            playerdetails.role=role
            playerdetails.COUNTRY=COUNTRY
            playerdetails.password=password
            playerdetails.confirmpassword=confirmpassword
            playerdetails.email=email
            playerdetails.fileupload=file
            playerdetails.save()
            return HttpResponse("data saved")
    return render(request,'display_form.html',{'form':form})

class DetailStudent(generics.ListCreateAPIView):
        queryset = Student5.objects.all()
        serializer_class = StudentSerializer


class DetailStudent1(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student5.objects.all()
    serializer_class = StudentSerializer






