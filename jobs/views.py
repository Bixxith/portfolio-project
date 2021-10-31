from django.shortcuts import render, get_object_or_404
from .models import Job
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

def contact(request):
    return render(request, 'jobs/contact.html')