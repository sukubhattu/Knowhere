from django import forms
from .models import Company

class CompanyModelForm(forms.ModelForm):
	class Meta:
		model  = Company
		fields = ['name', 'description']
