from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

import os
import ast
import json

# Create your views here.
def index(request):
    return render(request, "website/index.html")

def gsocyr(request, gsoc_yr):
    stat_json = 'website/static/data/'

    if gsoc_yr == 2016:
        json_yr = '2016.json'
    elif gsoc_yr == 2017:
        json_yr = '2017.json'
    elif gsoc_yr == 2018:
        json_yr = '2018.json'
    elif gsoc_yr == 2019:
        json_yr = '2019.json'
    elif gsoc_yr == 2020:
        json_yr = '2020.json'
    elif gsoc_yr == 2021:
        json_yr = '2021.json'
    else:
        return render(request, "website/amnesia.html")

    with open(os.path.join(settings.BASE_DIR, stat_json, json_yr)) as file:
        yeardata = ast.literal_eval(json.dumps(json.load(file)))

        yearnum =  int(yeardata["year"])
        yeardata = yeardata["organizations"]

    return render(request, "website/year.html", {
        "yr_num": yearnum,
        "yr_data": yeardata
    })

def oops(request, any_str):
    return render(request, "website/amnesia.html")





