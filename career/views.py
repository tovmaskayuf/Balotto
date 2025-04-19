from django.shortcuts import render

def career_home(request):
    return render(request, 'career/index.html')