from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from new.models import Article
from .models import Like

class LikeArticle(View):
    def post(self,request,slug):
        article=get_object_or_404(Article,slug=slug)
        like,created=Like.objects.get_or_create(article=article,user=request.user)

        if not created:
            like.delete()
        return redirect('detail_n',slug=slug)