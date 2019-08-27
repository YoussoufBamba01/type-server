from django import forms
from django.db import models

# Create your models here.
class Post (forms.Form):
	title = forms.CharField(label ='valeur', max_length=225)
	
