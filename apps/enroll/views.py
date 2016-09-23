from django.shortcuts import render, redirect, HttpResponse
from .models import Course

def index(request):
  
	
	context = {
	'courses': Course.objects.all(),
	
	}
	
	return render(request, 'enroll/index.html', context)

def addcourse(request):
	

	if request.method == 'POST':
		Course.objects.create(name = request.POST['name'], description = request.POST['description'])
	return redirect('/')

def delete(request, id):

	delcourse = Course.objects.get(id = id)
	
	context = {
    	'courses': delcourse
    }
	if request.method == 'GET':
		return render(request, 'enroll/destroy.html', context)

	delcourse.delete()