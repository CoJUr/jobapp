from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

job_title = [
    "First Job",
    "Second Job",
]

job_description = [
    "First job description",
    "Second job description"
]
# Create your views here.
# views (classes) defined here


def hello(request):
    for job_desc in job_description:
        htm = f"<div>{job_desc}</div>"

    for job in job_title:
        html = f"<li>{job}<li>"
    return HttpResponse("<h3>Hello World! Here are all the jobs:"+html + "</h3>" + htm)


def show_details(request, id):

    print(type(id))

    if id == 0:
        return redirect("/")

    return_html = f"<h1>{job_title[id]}</h1>  <h3>{job_description[id]}</h3>"
    return HttpResponse(return_html)
