import datetime

from django.http import HttpResponse
from django.shortcuts import render

from .forms import SubmitFibonacci

global fibonacci_sequence
fibonacci_sequence = [0, 1, 1]


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
            response_data["result"] = fibonacci_calculator(int(index))
            end_time = datetime.datetime.now().time().strftime('%H:%M:%S')
            response_data["elapsed"] = (
            datetime.datetime.strptime(end_time, '%H:%M:%S') - datetime.datetime.strptime(start_time, '%H:%M:%S'))
            return render(request, 'fibonacci_calculator.html', {'fibonacci_calculator': response_data})
    else:
        form = SubmitFibonacci()

    return render(request, 'index.html', {'form': form})


def fibonacci_calculator(n):
    try:
        if fibonacci_sequence[n]:
            return fibonacci_sequence[n - 1]
    except:
        for i in xrange(3, n):
            fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
        return fibonacci_sequence[-1]
