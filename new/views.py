from django.contrib.admin.templatetags.admin_list import pagination
from django.shortcuts import render,redirect,get_object_or_404
from django.template.defaultfilters import title
from django.template.defaulttags import comment
from unicodedata import category
from django.db.models import Q
from django.contrib.auth import login

from akkounts.models import User
from intractions.models import Comment
from .models import Article,Category
from django.core.paginator import Paginator

def home_page(request):
    latest_new=Article.published.all()[0]
    latest_new2=Article.published.all()[1:5]
    sport_new=Article.objects.filter(status='published',category__name='Sport')[0:4]
    texnology_new=Article.objects.filter(status='published',category__name='Texnologiya')[0:4]
    business_new=Article.objects.filter(status='published',category__name='Biznes')[0:4]
    xorij_new=Article.objects.filter(status='published',category__name='Xorij')[0:4]

    query=request.GET.get('q','')
    if query:
        articles=Article.published.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )
        return render(request, 'search.html', {"articles":articles})

    context={
        "latest_new":latest_new,
        "latest_new2":latest_new2,
        "sport_new":sport_new,
        'texnology_new':texnology_new,
        'business_new':business_new,
        'xorij_new':xorij_new,
    }


    return render(request,'index.html',context)

def delete_article(request, pk):
    article = get_object_or_404(Article, id=pk)

    if request.user == article.author:
        article.delete()

    return redirect('home')

def contact_page(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')

        User.objects.create(
            username=name,
            email=email

        )
        return redirect('home')

    return render(request,'contact.html')

def surovnoma(request):
    if request.method=="POST":
        name=request.POST.get('first_name')
        surname=request.POST.get('last_name')
        age=request.POST.get('age')
        email=request.POST.get('email')
        bio=request.POST.get('bio')
        telefon=request.POST.get('username')
        password = request.POST.get('password')


        user=User.objects.create_user(
            first_name=name,
            last_name=surname,
            age=age,
            email=email,
            bio=bio,
            username=telefon,
            password=password
        )
        login(request, user)
        return redirect('home')
    return render(request,'surovnoma.html')

def detail_page(request,slug):
    article=get_object_or_404(Article.published,slug=slug)
    comments=Comment.objects.filter(article=article,parent__isnull=True)
    viewed=request.session.get('viewed_articles',[])
    if article.id not in viewed:
        article.views_count+=1
        article.save()
        viewed.append(article.id)
        request.session['viewed_articles']=viewed

    if request.method=='POST':
        if not request.user.is_authenticated:
            return redirect('ariza')
        body=request.POST.get('body')
        parent_id=request.POST.get('parent_id')
        if body:
            Comment.objects.create(
                article=article,
                body=body,
                author=request.user,
                parent_id=parent_id,
            )
            return redirect('detail_n',slug=article.slug)

    context={
        "article":article,
        "comments":comments,
    }
    return render(request,'single-page.html',context)

def add_article(request):
    if request.method == "POST":
        title = request.POST.get("title")
        cover = request.FILES.get("cover")
        body = request.POST.get("body")
        category = request.POST.get("category")

        article = Article.objects.create(
            title=title,
            cover=cover,
            body=body,
            author=request.user,
            category_id=category,
            status="published"
        )

        return redirect("detail_n", slug=article.slug)

    categories = Category.objects.all()

    context = {
        "categories": categories
    }

    return render(request, "add_page.html", context)


def sport(request):
    sports_new=Article.published.filter(category__name='Sport')
    return render(request,'sport.html',{"sports_new":sports_new})

def xorij(request):
    xorijiy_new=Article.published.filter(category__name='Xorij')
    return render(request,'xorij.html',{"xorijiy_new":xorijiy_new})

def texnologiya(request):
    texnologiya=Article.published.filter(category__name='Texnologiya')
    paginator=Paginator(texnologiya,4)
    page=request.GET.get('page')
    texnologiya_new=paginator.get_page(page)
    return render(request,'texnologiya.html',{"texnologiya_new":texnologiya_new})



def biznes(request):
    biznes_new=Article.published.filter(category__name='Biznes')
    return render(request,'biznes.html',{"biznes_new":biznes_new})

def mahalliy(request):
    mahalliy_new=Article.published.filter(category__name='Mahalliy')
    return render(request,'mahalliy.html',{"mahalliy_new":mahalliy_new})
