from django.shortcuts import render

from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

from web.models import User,Expense,Income,Token
from datetime import datetime
# Create your views here.

@csrf_exempt
def submit_income(request):

    """submit income"""
    #TODO: validated data

    this_token = request.POST.get('token')
    this_user = User.objects.filter(token__token = this_token).get()

    if 'date' not in request.POST:
        date = datetime.now()
    else:
        date= request.POST['date']

    Income.objects.create(user = this_user , text = request.POST['text'] , amount= request.POST['amount'] , date = date)

    return JsonResponse({
        'status' : 'ok',
    },encoder=json.JSONEncoder)

@csrf_exempt
def submit_expense(request):

    """submit expense"""
    #TODO: validated data

    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()

    if 'date' not in request.POST:
        date = datetime.now()
    else:
        date= request.POST['date']

    Expense.objects.create(user = this_user , text = request.POST['text'] , amount= request.POST['amount'] , date = date)

    return JsonResponse({
        'status' : 'ok',
    },encoder=json.JSONEncoder)
