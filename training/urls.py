from django.urls import path
from . import views

app_name = "training"

urlpatterns = [
    path('', views.HomeView.as_view(), name = "home"),
    path('contact/', views.ContactView.as_view(), name = "contact"),
    path('portfolio/', views.PortfolioView.as_view(), name = "portfolio"),
]