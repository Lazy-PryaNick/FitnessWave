from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from django.conf import settings
from .models import (
    Product,
)
from . forms import ContactForm

# Create your views here.
class HomeView(generic.TemplateView):
	template_name = "home.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		portfolio = Product.objects.filter(is_available = True)
		context["portfolio"] = portfolio
		return context

class ContactView(generic.FormView):
	template_name = "contact.html"
	form_class = ContactForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Спасибо! Менеджер скоро с Вами свяжется!')
		return super().form_valid(form)


class PortfolioView(generic.ListView):
	model = Product
	template_name = "portfolio.html"
	paginate_by = 10

	def get_queryset(self):
		return super().get_queryset()

