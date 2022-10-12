from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
from django.template import loader

job_title = [
    "First Job",
    "Second Job",
    "Third Job"
]

job_description = [
    "First job description",
    "Second job description",
    "Third job description"
]
# Create your views here.
# views (classes) defined here


def hello(request):
    template = loader.get_template('app/hello.html')
    context = {}
    return HttpResponse(template.render(context, request))
# def hello(request):
#     for job_desc in job_description:
#         htm = f"<div>{job_desc}</div>"

#     for job in job_title:
#         html = f"<li>{job}<li>"
#     return HttpResponse("<h3>Hello World! Here are all the jobs:"+html + "</h3>" + htm)


def job_list(request):

    list_of_jobs = "<ul>"
    for j in job_title:
        job_id = job_title.index(j)
        detail_url = reverse('jobs_detail', args=(job_id,))
        list_of_jobs += f"<li><a href='{detail_url}'>{j}</a> </li>"
    list_of_jobs += "</ul>"
    return HttpResponse(list_of_jobs)


def show_details(request, id):

    print(type(id))

    try:
        if id == 0:
            return redirect(reverse('jobs_home'))

        return_html = f"<h1>{job_title[id]}</h1>  <h3>{job_description[id]}</h3>"
        return HttpResponse(return_html)

    except:
        return HttpResponseNotFound("Not found")
