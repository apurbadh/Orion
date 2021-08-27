from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    full_name = models.CharField(null=True, max_length=200)
    description = models.TextField(null=True)
    profile_pic = models.ImageField(null=True, upload_to='images')
    
    def __str__(self):
        return self.user.username   

class Community(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField()
    users = models.ManyToManyField(User, related_name="users")
    admins = models.ManyToManyField(User, related_name="admins")
    profile = models.ImageField(upload_to="community")
    banner = models.ImageField(upload_to="community") 
    
    def __str__(self):
        return self.name  
    
    class Meta:
        verbose_name_plural = "Communities" 

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    community = models.ForeignKey(Community, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=256)
    description = RichTextField()
    likes = models.ManyToManyField(User, related_name="likes")
    created_on = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
        
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="com_likes")
    comment = RichTextField()
    created_on = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username