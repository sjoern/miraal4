from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponse
from django.template import loader
from django.db.models import Sum
from .models import FinesList, PlayerFines, Players
import pandas as pd

# Create your views here.
def home_page(request):

    template = loader.get_template('home_page.html')

    return HttpResponse(template.render())


def fines(request):

    template = loader.get_template('fines_page.html')

    data = FinesList.objects.all()

    fines = PlayerFines.objects.all()

    groupedFines = PlayerFines.objects.values('player_name__player').filter(player_paid=False).annotate(total_cost=Sum('player_cost'))

    return render(request, 'fines_page.html', {'data': data, 'fines': fines,
                                               'groupedFines': groupedFines})


