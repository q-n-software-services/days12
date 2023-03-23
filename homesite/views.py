import datetime
from bs4 import BeautifulSoup
import requests
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import ayyaam,suggestons, subscriptions, dateStore
from django.utils import timezone
# Create your views here.


def find_islamic_date():
    date = dateStore.objects.all()

    date = date[0]

    mahina = date.IslamicMonth

    saal = date.IslamicYear

    # print("Saaal = ", saal)

    now = datetime.datetime.now()

    date1 = datetime.datetime(int(date.startYear), int(date.startMonth), int(date.startDate))
    date2 = datetime.datetime(now.year, now.month, now.day)
    delta = date2 - date1
    days = delta.total_seconds() / 60 / 60 / 24

    return int(days), int(mahina), int(saal)


def homepage(request):
    date = find_islamic_date()

    mydata = ayyaam.objects.all().order_by("mydate")
    matched_data = []
    now = datetime.datetime.now()
    today = [['''الصلوة والسلام عليك يا سيدي يا رسول الله\n
صلي الله عليه وآله وسلم\n\n
الصلوة والسلام عليك يا سيدي يا حبيب الله\n
صلي الله عليه وآله وسلم\n''']]

    done = False
    for i, data in enumerate(mydata):
        if data.month == str(date[1]):
            if data.mydate == date[0]:
                if done == False:
                    today = []
                    done = True
                today.append([data.title, data.details, data.month_islamic_title, data.details_page_link, data.mydate, data.month, i])

            matched_data.append((data.title, data.details, data.month_islamic_title, data.details_page_link, data.mydate, data.month, i))
    # mydata = [ for item in mydata]
    month_numbers = {
        '1': 'محرم الحرام',
        '2': 'صفرالمظفر',
        '3': 'ربیع الاول',
        '4': 'ربیع الثانی',
        '5': 'جمادی الاول',
        '6': 'جمادی الثانی',
        '7': 'رجب المرجب',
        '8': 'شعبان العظم',
        '9': 'رمضان المبارک',
        '10': 'شوال المکرم',
        '11': 'ذیقعدہ الحرام',
        '12': 'ذوالحجۃ الحرام'
    }

    stuff_for_frontend = {'data': matched_data, 'today': today, 'islamic_date': date[0], 'islamic_month': date[1], "islamic_month_name":  month_numbers[str(date[1])], "saal": date[2]}
    # stuff_for_frontend = {'data': matched_data, 'today': today, 'islamic_date': 'str(date.tareekh)', 'islamic_month': 'str(date.month_islamic)', "islamic_month_name": "Muhammad Mohib"}

    return HttpResponse("Muhammad Mohib")
# render(request, 'home.html', stuff_for_frontend)


@csrf_exempt
def suggestions(request):
    currentdate = timezone.now()
    content = request.POST["data"]
    created_obj = suggestons.objects.create(added_date=currentdate, text=content)
    return HttpResponseRedirect('/')


@csrf_exempt
def subscribe(request):
    currentdate = timezone.now()
    content = request.POST["email"]
    created_obj = subscriptions.objects.create(added_date=currentdate, text=content)
    return HttpResponseRedirect('/')
