from django.urls import path
from .views import LikeArticle

urlpatterns=[
    path('like/<slug:slug>/',LikeArticle.as_view(),name='like'),
]