from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Members
from django.urls import reverse

# Create your views here.
def new(req):
    mymembers=Members.objects.all().values()
    template=loader.get_template('index.html')
    context={
        'mymembers':mymembers,
    }
    return HttpResponse(template.render(context,req))
def add(request):
    template=loader.get_template('add.html')
    return HttpResponse(template.render({},request))
def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    z=request.POST['dob']
    member = Members(firstname=x, lastname=y, dob=z)
    member.save()
    return HttpResponseRedirect(reverse('index'))
def delete(request, id):
     member = Members.objects.get(id=id)
     member.delete()
     return HttpResponseRedirect(reverse('index'))
def update(request, id):
     mymember = Members.objects.get(id=id)
     template = loader.get_template('update.html')
     context = {
         'mymember': mymember,
        }
     return HttpResponse(template.render(context, request))
def updaterecord(request, id):
    first = request.POST['first']
    last = request.POST['last']
    dob=request.POST['dob']
    member = Members.objects.get(id=id)
    member.firstname = first
    member.lastname = last
    member.dob=dob
    member.save()
    return HttpResponseRedirect(reverse('index')) 

    
