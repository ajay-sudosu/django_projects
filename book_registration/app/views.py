from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.db.models import Q
from .models import User


def show(request):
	context={'list':User.objects.all()}
	return render(request,'app/home.html',context)


def register(request):
	if request.method=='POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,f'Your data has been saved.')
			return redirect('home')
	else:
		form=RegistrationForm()
	return render(request,'app/register_form.html',{'form':form})


def search(request):
	if request.method=="GET":
		query=request.GET['query']
		if query:
			data=User.objects.filter(
									Q(genere__icontains=query)| 
									Q(language__icontains=query)|
									Q(book_name__icontains=query)|
									Q(author__icontains=query)
									)
			context={'data':data,'query':query}
			return render(request,'app/search.html',context)
		else: 
			return render(request,'app/search1.html')