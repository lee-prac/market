from django.urls import path
from . import views

urlpatterns = [
    path('', views.product,name='product'),
    path('detail/', views.detail,name='detail'),
    path('update/', views.update,name='update'),
]