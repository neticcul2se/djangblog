from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


def Hello(request):
    # Query data from models
    data = Post.objects.all()
    return render(request, 'index.html', {'datas': data})


def page1(request):
    return render(request, 'page1.html')


def createForm(request):
    return render(request, 'form.html')


def addBlog(request):
    name = request.POST['name']
    des = request.POST['des']
    return render(request, 'result.html', {'name': name, 'des': des})


def loginform(request):
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def logincheck(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return redirect('/')
    else:
        messages.info(request, 'ไม่พบข้อมูล')
        return redirect('/login')


def fmregister(request):
    return render(request, 'register.html')


def register1(request):
    username = request.POST['username']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    repassword = request.POST['repassword']

    if password == repassword:
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username นี้มีคนใช้แล้ว')
            return redirect('/fmregister')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email นี้มีคนใช้แล้ว ')
            return redirect('/fmregister')
        else:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=firstname,
                last_name=lastname
            )
            user.save()
            return redirect('/')
    else:
        messages.info(request, 'รหัสไม่ตรงกัน')
        return redirect('/fmregister')
