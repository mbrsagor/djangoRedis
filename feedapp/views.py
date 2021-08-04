from django.shortcuts import render
from rest_framework import views, status
from rest_framework.response import Response


def index(request):
    return render(request, 'feedapp/index.html')


def reports(request):
    return render(request, 'feedapp/reports.html')
