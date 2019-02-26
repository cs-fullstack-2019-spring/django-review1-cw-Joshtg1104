from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse


# Create your views here.

def index(request):
    print("Don don don")

    return render(request, 'pageCocktail_app/home.html')


def p2(request):
    print("Boop")

    return render(request, 'pageCocktail_app/page2.html')


def p3(request):
    print("Woop woop")

    return render(request, 'pageCocktail_app/page3.html')


def p4(request):
    print("Yep")

    return render(request, 'pageCocktail_app/page4.html')


def p5(request):
    print("Jump")

    return render(request, 'pageCocktail_app/page5.html')
