from django.shortcuts import render


def index(request):
    return render(request, 'feedapp/index.html')


def reports(request):
    return render(request, 'feedapp/reports.html')
