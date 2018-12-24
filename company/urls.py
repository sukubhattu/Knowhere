from django.urls import path
from . import views
from .views import CompanyListView, CompanyDetailView, CompanyCreateView, CompanyUpdateView, CompanyDeleteView
urlpatterns = [
	path('', CompanyListView.as_view(), name = 'company_list'),
	path('<int:pk>/', CompanyDetailView.as_view(), name = 'company_detail'),
	path('create/', CompanyCreateView.as_view(), name = 'company_create'),
	path('<int:pk>/update/', CompanyUpdateView.as_view(), name = 'company_update'),
	path('<int:pk>/delete/', CompanyDeleteView.as_view(), name = 'company_update'),
	path('funcreate/', views.create_company, name = 'create_company'),
]
