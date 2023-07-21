from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def start(request):
    return render(request,'media/index.html')


