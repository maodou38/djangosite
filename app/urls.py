from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'moments_input',views.moments_input), #新增
    url(r'',views.welcome),
]