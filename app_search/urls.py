from django.urls import path 

from . import views 


urlpatterns = [ 
    path('', views.search, name='search'),
    path('csv', views.get_csv, name='get_csv'),
]
