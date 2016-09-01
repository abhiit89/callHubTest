import datetime
from math import sqrt
from django.http import HttpResponse
from django.shortcuts import render
from .forms import SubmitFibonacci

def index(request):
    return HttpResponse("Hello, world. You're at the Fibonacci Page.")

def save_fibonacci(request):
    start_time = datetime.datetime.now().time().strftime('%H:%M:%S')
    if request.method == "POST":
        form = SubmitFibonacci(request.POST)
        if form.is_valid():
            index = form.cleaned_data['index']
            response_data = {}
            response_data["index"] = int(index)
            response_data["result"] = int(F(int(index)))
            end_time = datetime.datetime.now().time().strftime('%H:%M:%S')
            response_data["elapsed"] = (datetime.datetime.strptime(end_time,'%H:%M:%S') - datetime.datetime.strptime(start_time,'%H:%M:%S'))
            return render(request, 'fibonacci.html', {'fibonacci': response_data})
    else:
        form = SubmitFibonacci()

    return render(request, 'index.html', {'form': form})

def F(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))