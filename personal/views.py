from django.shortcuts import render

def home_screen_view(request):
    return render(request, 'base.html')

def news(request):
    return render(request, 'news.html')

def ev(request):
    return render(request,'personal/home.html')