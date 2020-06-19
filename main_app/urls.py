from django.urls import path
from . import views
from .views import PopList

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pops/', views.PopList.as_view(), name='pops_index'),
    path('pops/<int:pk>/', views.PopDetail.as_view(), name='pops_detail'),
    path('pops/create/', views.PopCreate.as_view(), name='pops_create'),
    path('pops/<int:pk>/update/', views.PopUpdate.as_view(), name='pops_update'),
    path('pops/<int:pk>/delete/', views.PopDelete.as_view(), name='pops_delete'),
    path('pops/<int:pop_id>/add_limited/', views.add_limited, name='add_limited'),
    path('pops/<int:pop_id>/assoc_accessory/<int:accessory_id>/', views.assoc_accessory, name='assoc_accessory'),
]