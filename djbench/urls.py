from django.conf.urls import url
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<pk>\d+)/$', views.entity, name='article'),
    url(r'^$', views.index, name='index')
]
