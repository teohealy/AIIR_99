from django.shortcuts import render
from django.http import HttpResponse
import parsing


# Create your views here.


def index(request, a, b):
    return HttpResponse(f"Сумма чисел {a} + {b} равна {parsing.summary(a, b)}")