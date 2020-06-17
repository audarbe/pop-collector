from django.urls import path
from . import views
from .views import PopList

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pops/', views.PopList.as_view(), name='pops_index'),
    path('pops/<int:pk>/', views.PopDetail.as_view(), name='pops_detail'),
]