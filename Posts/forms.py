from django import forms
from django.db import models

# Create your models here.
class Post (forms.Form):
	title = forms.CharField(label ='titre', max_length=225)
	body = forms.CharField(label ='corps')
