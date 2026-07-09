from django.shortcuts import render,get_object_or_404
from .models import Profile

def profile_page(request,pk):
    user=get_object_or_404(Profile,id=pk)
    context={
        "user":user
    }
    return render(request,'profile.html',context)






