from django import forms
from django.shortcuts import render
from django.forms import ModelForm
from bootstrap_datepicker_plus import DatePickerInput

BIRTH_YEAR_CHOICES = ('1980', '1981', '1982', '1983', '1984', '1985', '1986')


class SimpleForm(forms.Form):
    birth = forms.DateField(widget=forms.SelectDateWidget(years=range(1950,2020)))

def form_test(request):

	form = SimpleForm()
	return render(request, "test.html", {'form': form})


