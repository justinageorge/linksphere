from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile",null=True)
    address=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    profile_pic=models.ImageField(upload_to="profilepics",null=True,blank=True)#null is for data base and blank is for form so that it will not be included in form
    dob=models.DateField(null=True)
    bio=models.CharField(max_length=200,null=True)
    following=models.ManyToManyField("self",related_name="followed_by",symmetrical=False,null=True)#there is no need of someone to follow back
    block=models.ManyToManyField("self",related_name="blocked", symmetrical=False,null=True)

    def __str__(self):
        return self.user.username #we are goimg from userprofile to usermodel ie to print the profile name
# Create your models here.
class Posts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="userpost")
    title=models.CharField(max_length=200)
    post_image=models.ImageField(upload_to="posters",null=True,blank=True)
    created_date=models.DateTimeField(auto_now_add=True)
    liked_by=models.ManyToManyField(User,related_name="post_like")

    def __str__(self):
        return self.title
    

class Comments(models.Model):
    user=models.ForeignKey(User,related_name="comments",on_delete=models.CASCADE)
    text=models.CharField(max_length=200)
    created_date=models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey(Posts,related_name="post_comments",on_delete=models.CASCADE)

    def __str__(self):
        return self.text
    
class stories(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="userstories")
    title=models.CharField(max_length=200)
    post_image=models.ImageField(upload_to="stories",null=True,blank=True)
    created_date=models.DateTimeField(auto_now_add=True) #to set date automatically auto_now_add
    # exp=created_date+timezone.timedelta(days=1)
    expiry_date=models.DateTimeField()#to generate query file we apply make migrations and to run the file we apply makemigrate
   
    def __str__(self):
        return self.title


    def save(self,*args,**kwargs):
        if not self.expiry_date:
            self.expiry_date=timezone.now()+timezone.timedelta(days=1)
        super().save(*args,**kwargs)    
#python manage.py makemigrations
#python manage.py migrate

def create_profile(sender,created,instance,**kwargs):
    if created:
         UserProfile.objects.create(user=instance)
post_save.connect(create_profile,sender=User)         



