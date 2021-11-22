from django.shortcuts import render

def first_html(request):
    return render(request,'h1.html')

def  second_html(request):
    return render(request,'h2.html')
    