from django.urls import path
from . import views
from .views import CompanyListView, CompanyDetailView
urlpatterns = [
	path('', CompanyListView.as_view(), name = 'company_list'),
	path('<int:pk>/', CompanyDetailView.as_view(), name = 'company_detail'),
	path('create/', views.create_company, name = 'create_company'),
]
