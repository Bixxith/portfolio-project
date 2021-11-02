from django.shortcuts import render, get_object_or_404
from .models import Job
import requests
import json

# Create your views here.
def homepage(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})

def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    print(job_detail)
    return render(request, 'jobs/detail.html', {'job':job_detail})

def portfolio(request):
    jobs = Job.objects
    return render(request, 'jobs/portfolio.html', {'jobs':jobs})

def aboutme(request):
    return render(request, 'jobs/aboutme.html')

def blog(request):
    return render(request, 'jobs/blog.html')

def devto(request):
    response = requests.get('https://dev.to/api/articles?username=bixxith')
    data2 = response.json()
    otherDict = dict()
    newDict = dict()

    for i in range(len(data2)):
        newDict[data2[i]['id']] = [data2[i]['title'],data2[i]['url'],data2[i]['tags'],data2[i]['created_at'],data2[i]['comments_count'],data2[i]['positive_reactions_count'],data2[i]['cover_image']]

    otherDict['blogdata'] = newDict

    return render(request, 'jobs/blog.html', otherDict)
