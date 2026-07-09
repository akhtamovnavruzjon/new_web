from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio=models.TextField(verbose_name="Bio",default=" ")
    age=models.IntegerField(default=0)




class Profile(models.Model):
    user   = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    avatar = models.ImageField(upload_to='avatars/',blank=True,null=True)
    bio    = models.TextField()

    def __str__(self):
        return F"{self.user.username} profili"

