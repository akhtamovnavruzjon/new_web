from django.urls import path
from akkounts.views import profile_page
from new.urls import urlpatterns

urlpatterns=[
    path('profile/<int:pk>/',profile_page,name='profil')
]


