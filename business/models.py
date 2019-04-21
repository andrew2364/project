from django.db import models
from django import forms


class Arkans(models.Model):
	arkan_number = models.IntegerField(unique=True)
	cel = models.TextField(max_length=1000)
	osnova = models.TextField(max_length=1000)
	jertva = models.TextField(max_length=1000)

class BusinessForm(forms.Form):
	name = forms.CharField(label='Ваше имя', max_length=50, required=False)
	business_name = forms.CharField(label='Название бизнеса', max_length=200)