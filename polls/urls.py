from django.urls import path
"""frtgvhyujl"""
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.his, name='his'),
    path('', views.geo, name='geo'),
    path('', views.hq1, name='hq1'),
    path('', views.hq2, name='hq2'),
    path('', views.hq3, name='hq3'),
    path('', views.gq1, name='gq1'),
    path('', views.gq2, name='gq2'),
    path('', views.gq3, name='gq3'),
    path('', views.empty, name='empty')
]
