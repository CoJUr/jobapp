from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

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

    print(type(id))

    if id == 0:
        return redirect("/")

    return_html = f"<h1>{job_title[id]}</h1>  <h3>{job_description[id]}</h3>"
    return HttpResponse(return_html)
