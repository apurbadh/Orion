from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Profile, Community, Comment
from django import forms

class UserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ["title", "community", "description"] 
        
class CommunityForm(forms.ModelForm):
    
    class Meta:
        model = Community
        fields = ["name", "description", "profile", "banner"]
        
class SettingForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ["full_name", "description", "profile_pic"]
        
class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ["comment"]