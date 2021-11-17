from django.shortcuts import render


def home(request):
    return render(request, 'jtalks/home.html')

def about(request):
    return render(request, 'jtalks/about.html')

