from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name="home"),
    path('material/<slug>', views.product_detail, name="material"),
    path('catalog/', views.CatalogPage.as_view(), name="catalog"),
]


