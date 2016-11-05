from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^wx$', views.widget_list, name='widget_list'),
]
