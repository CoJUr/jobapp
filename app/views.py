from django.shortcuts import render
from django.http import HttpResponse

job_title = [
    "First Job",
    "Second Job"
]

job_description = [
    "First job description",
    "Second job description"
]
# Create your views here.
# views (classes) defined here


def hello(request):
    return HttpResponse("<h3>Hello World</h3>")


def show_details(request, id):
    # return HttpResponse(f"<h3>Job detail page {id}<h3>")
    # site = "https://google.com"
    return_html = f"<h1>{job_title[id]}</h1>  <h3>{job_description[id]}</h3>"
    return HttpResponse(f"Visit <a href={site}>Google here </a>")
