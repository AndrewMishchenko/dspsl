from django.conf.urls import url

from . import views

app_name = 'products'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_like/$', views.likes, name='add_like'),
    url(r'^add_comment/$', views.add_comment, name='add_comment'),
    url(r'^(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]
