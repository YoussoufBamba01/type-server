from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.

from . forms import Post


def home(request):

	return render (request, "pages/home.html")

def post(request):

	return render (request, "pages/post.html")

def show(request):
	from . import sensorsdata

	if request.method == 'POST':
		
		form=Post(request.POST)

		if form.is_valid():
			recordata(form.data)
			
			return render(request, 'pages/show.html', {'form': form})

		else:
			return render(request, 'pages/post.html')

	else:
		form=Post()
		return render(request, 'pages/post.html')


    

      	


