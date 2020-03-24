from django.shortcuts import render, HttpResponse, redirect
from bs4 import BeautifulSoup as BS
import requests
import json


def page(url):
    page = requests.get(url)
    soup = BS(page.content, 'html.parser')
    return soup

def ByCountry(request):
    url = "https://ncov.dxy.cn/ncovh5/view/en_pneumonia?from=dxy&source=&link=&share="
    soup = page(url)

    byCountry = soup.find('script', attrs = {'id':'getListByCountryTypeService2true'})

    byCountry = byCountry.text[48:]
    byCountry = byCountry[:-11]

    byCountry = str(byCountry)
    byCountry = byCountry.replace("Syrian\xa0ArabRepublic", "Syrian Arab Republic")
    byCountry = byCountry.replace("'", '"')
    byCountry = json.dumps(byCountry)
    return HttpResponse(byCountry, content_type="application/json")

def globalData(request):
    url = "https://ncov.dxy.cn/ncovh5/view/en_pneumonia?from=dxy&source=&link=&share="
    soup = page(url)
    globalData = soup.find('script', attrs = {'id':'getStatisticsService'})

    globalData = globalData.text[36:]
    globalData = globalData[:-11]
    globalData = json.dumps(globalData)
    globalStatistics = json.loads(globalData)

    return HttpResponse(globalStatistics,  content_type="application/json")



def index(request):

    # ByCountry = json.loads(ByCountry())

    response_data = {}
    response_data['result'] = 'error'
    response_data['message'] = 'Some error message'
    data = json.dumps(response_data)
    return HttpResponse(data, content_type="application/json")
