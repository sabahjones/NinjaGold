import random
from django.shortcuts import render, redirect

def index(request):
    if 'history' not in request.session:
        request.session['history'] = []
        request.session['total'] = 0
    return render(request, 'view_controller/index.html')

def get_gold(request):
    gold = {
        'farm': random.randrange(9, 21),
        'cave': random.randrange(4, 11),
        'house': random.randrange(1, 6),
        'casino': random.randrange(-51, 50),
    }

    location = ''

    if 'farm' in request.POST:
        location = 'farm'
    elif 'cave' in request.POST:
        location = 'cave'
    elif 'house' in request.POST:
        location = 'house'
    elif 'casino' in request.POST:
        location = 'casino'

    request.session['total'] += gold[location]
    request.session['history'].append(gold[location])
    
    return redirect('/')
