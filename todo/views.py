from django.shortcuts import render,redirect
from datetime import datetime
from . models import task
from .forms import todolistForm
from django.contrib import messages

# Create your views here.
def home(request):
	List = task.objects.all
	myname = "Er Qureshi Faheem"
	today = datetime.now()

	if request.method == 'POST':
		form = todolistForm(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request,("------>data added"))
			List = task.objects.all
			return render(request,'home.html',{'name':myname,'done':today,'list':List})

	else:
		List = task.objects.all
		return render(request,'home.html',{'name':myname,'done':today,'list':List})


def aboutus(request):
	return render(request,'aboutus.html',{})


def delete(request,task_id):
	item = task.objects.get(pk=task_id)
	item.delete()
	messages.success(request, ('Item Has Been Deleted!'))
	return redirect('home')
