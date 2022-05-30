import random

from django.shortcuts import render
import random


def password(request):
    length = request.GET.get('Length')
    passwords = ''
    chrs = [chr(i) for i in range(97,97+26)]
    upper = [chr(i) for i in range(65,65+26)]
    nums = [str(i) for i in range(0,10)]
    spcial = '!@#$%^&*()_+'
    if request.GET.get('char'):
        chrs.extend(upper)
    if request.GET.get('schar'):
        chrs.extend(spcial)
    if request.GET.get('num'):
        chrs.extend(nums)
    if request.GET.get('Length'):
        for i in range(int(length)):
            passwords += str(random.choice(chrs))
    else:
        for i in range(11):
            passwords += str(random.choice(chrs))
    return render(request, 'password.html',{'password':passwords})

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')
