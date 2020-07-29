from django.shortcuts import render

def home_screen_view(request):
    people = ['ersegun', 'ertugrul', 'yildirim']
    context = {}
    context['people'] = people
    return render(request, 'base.html', context)

def news(request):
    return render(request, 'news.html')

def ev(request):
    return render(request,'personal/home.html')