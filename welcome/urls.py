from django.conf.urls import url
from . import views
 
urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^girls/$', views.girl_view, name='girl_view'),
	url(r'^guys/$', views.guy_view, name='guy_view'),
	url(r'^freshers/$', views.fresher_view, name='fresher_view'),	

]
 