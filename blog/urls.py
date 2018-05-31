from django.conf.urls import url
from . import views

urlpatterns = [
        # view named as post_list is allocated to the '^$' url
        url(r'^$', views.post_list, name='post_list'),
]
