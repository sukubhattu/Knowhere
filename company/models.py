from django.db import models
from django.contrib.auth.models import User
#for the reverse url
from django.urls import reverse

# Create your models here.
class Company(models.Model):
	name 		= models.CharField(max_length = 100)
	description = models.TextField(null = True)
	owner 		= models.ForeignKey(User, on_delete = models.CASCADE)
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		# return reverse('company_list')
		#if want to redirect to its detail page then
		return reverse('company_detail' ,kwargs = {'pk' : self.pk})