from pydoc import pager

from django.urls import path
from .views import home_page,contact_page,detail_page,sport,biznes,mahalliy,xorij,texnologiya,surovnoma,add_article,delete_article
from akkounts.views import profile_page


urlpatterns=[
    path('',home_page,name='home'),
    path('contact/',contact_page,name='contact'),
    path('new/<slug:slug>/',detail_page,name='detail_n'),
    path('sport/', sport, name='sport'),
    path('biznes/', biznes, name='biznes'),
    path('mahalliy/', mahalliy, name='mahalliy'),
    path('xorij/', xorij, name='xorij'),
    path('texnologiya/', texnologiya, name='texnologiya'),
    path('surovnoma/', surovnoma, name='ariza'),
    path('article/add/', add_article, name='add_article'),
    path('article/delete/<int:pk>/', delete_article, name='delete_article'),

]










