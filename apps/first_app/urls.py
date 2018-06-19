from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^process_gold', views.process_gold),
	url(r'^$', views.index),
]