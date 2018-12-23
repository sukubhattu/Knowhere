from django.shortcuts import render, redirect
from .forms import CompanyModelForm
from django.views.generic import ListView, DetailView
from .models import Company
from django.contrib.auth.decorators import login_required

# Create your views here.
class CompanyListView(ListView):
	model = Company
	context_object_name = 'companies'
	template_name = 'company/companies_list.html'

class CompanyDetailView(DetailView):
	model = Company
	template_name = 'company/company_detail.html'

@login_required
def create_company(request):
	form = CompanyModelForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('company_list')
	return render(request, 'company/create_company.html', {'form': form})

