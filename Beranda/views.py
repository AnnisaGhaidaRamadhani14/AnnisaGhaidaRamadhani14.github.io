from django.shortcuts import render

# Create your views here.

def web2(request):
    return render(request, 'index2.html')