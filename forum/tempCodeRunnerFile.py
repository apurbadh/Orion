from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from .models import Profile, Post, Community, Comment
from django.contrib.auth.models import User


# Register your models here.
class OrionAdmin(AdminSite):
    site_title = ugettext_lazy("Orion Admin")
    site_header = ugettext_lazy("Admin Panel")
    index_title = ugettext_lazy("Index")
    
admin.site = OrionAdmin()

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Community)
admin.site.register(Comment)
admin.site.register(User)