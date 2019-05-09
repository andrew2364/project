from django import forms
from django.db import models


class Arkans(models.Model):

	arkan_number = models.IntegerField(unique=True)
	cel = models.TextField(max_length=1000)
	osnova = models.TextField(max_length=1000)
	jertva = models.TextField(max_length=1000)

class BusinessForm(forms.Form):

	name = forms.CharField(label='Ваше имя ', max_length=50, required=False)
	birth = forms.DateField(required = False, label='День рождения ', widget=forms.SelectDateWidget(years=range(1930, 2020)))
	business_name = forms.CharField(label='Название бизнеса ', max_length=200)



