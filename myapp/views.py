from django.shortcuts import render, render_to_response
from django.http import HttpRequest

# Create your views here.
def index(request):
    return render_to_response('index.html')

def add(request):

    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    res = val1 + val2

    return render(request, 'results.html', {'result':res})