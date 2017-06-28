from django.shortcuts import render, render_to_response
from . models import credit_card_details
# Create your views here.
#
# def index(request):
#     return render(request, 'index.html');

def index(request):
    return render_to_response('index.html', {'credit': credit_card_details.objects.all()})