from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='payments_index'),
    path('esewa_payment_success', views.success, name='esewa_success'),
    path('esewa_payment_failed', views.failed, name='esewa_failure'),
    
]