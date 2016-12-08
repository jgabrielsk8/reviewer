from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^list/$', views.ReviewList.as_view(), name='reviews'),
]
