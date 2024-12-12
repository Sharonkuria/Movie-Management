from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from django.contrib import messages, auth
from django.contrib import messages
from . forms import MovieForm

# Create your views here.
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('movieapp:index')
        else:
            messages.info(request,"invalid login details!")
            return redirect('/')
        return render(request,"login.html")
    return render(request,"login.html")

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request,"Username Already Taken!")
            return redirect('movieapp:signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request,"Email Already Taken!")
            return redirect('movieapp:signup')
        else:
            user=User.objects.create_user(username=username,email=email,password=password)
            user.save()
        return redirect('/')
    return render(request,"signup.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def index(request):
    movie=Movie.objects.all()
    context={
        'movie_list':movie
    }
    return render(request,'index.html',context)

def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':movie})
    

def add(request):
    if request.method=="POST":
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        img=request.FILES['img']
        movies=Movie(name=name,desc=desc,year=year,img=img)
        movies.save()
        messages.info(request,"---Added Succesfully---")
        return redirect('movieapp:index')
    return render(request,'add.html')

def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('movieapp:index')
    return render(request,'edit.html',{'form':form,'movie':movie})  

def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('movieapp:index')
    return render(request,'delete.html')

def about(request):

    return render(request,'about.html')

    