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
            response_data["result"] = fibonacci(int(index))
            end_time = datetime.datetime.now().time().strftime('%H:%M:%S')
            response_data["elapsed"] = (datetime.datetime.strptime(end_time,'%H:%M:%S') - datetime.datetime.strptime(start_time,'%H:%M:%S'))
            return render(request, 'fibonacci.html', {'fibonacci': response_data})
    else:
        form = SubmitFibonacci()

    return render(request, 'index.html', {'form': form})

def fibonacci(n):
    f = [0,1,1]
    for i in xrange(3,n):
        f.append(f[i-1] + f[i-2])
    return f[-1]