from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

from . forms import Post


def home(request):

	return render (request, "pages/home.html")

def post(request):

	return render (request, "pages/post.html")

def error(request):
	return render(request, 'pages/error.html')

def show(request):
	from . import sensorsdata

	if request.method == 'POST':
		form = Post(request.POST)
		value = form.data

		if value.is_valid():
			return HttpResponse( "post vide de contenu")
				
		else:
			
			sensorsdata.recordata(value)
			return render(request, 'pages/show.html', {'form': form.data})	

	else:
		form=Post()
		return render(request, 'pages/error.html')



		


    

      	


