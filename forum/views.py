from django.shortcuts import redirect, render
from .forms import UserForm, PostForm, CommunityForm, SettingForm, CommentForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Comment, Community, Profile, Post
from django.contrib.auth.models import User
from .decorators import not_loggedin
from django.db.models import Q


# Create your views here.
@login_required(login_url="/login")
def logoutUser(req):
    logout(req)
    return redirect("/login")

def index(req):
    return render(req, "index.html")


def community(req, id):
    if req.method == "POST":
        community = Community.objects.get(id=id)
        community.users.add(req.user)
        return redirect('/c/' + str(id))
    isInCommunity = False
    try:
        community = Community.objects.get(id=id)
        if req.user in community.users.all():
            isInCommunity = True
        posts = Post.objects.all().filter(community=community)
    except:
        community = None
        posts = []
    context = {
        "community" : community,
        "posts" : posts,
        "joined" : isInCommunity
    }
    return render(req, "community.html", context)


@login_required(login_url="/login")
def create(req):
    try:
        c = int(req.GET.get("c"))
    except:
        c = 1
    form = PostForm()
    if req.method == "POST":
        form = PostForm(req.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = req.user
            task.save()
            return redirect('/post/' + str(task.id))
        else:
            messages.error(req, "Invalid information provided !")
            return redirect('/create')
    context = {
        "form" : form,
        "c" : c
    }
    return render(req, "create.html", context)

@not_loggedin
def loginPage(req):
    if req.method == "POST":
        username = req.POST["username"]
        password = req.POST["password"]
        user = authenticate(req, username=username, password=password)
        if user is not None:
            login(req, user)
            return redirect('/')
        else:
            messages.error(req, "Username or Password Incorrect !")
            return redirect('/login')
        
    return render(req, "login.html")


def post(req, id):
    if req.method == "POST":
        form = CommentForm(req.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.user = req.user;
            result.post = Post.objects.get(id=id)
            result.save()
            return redirect("/post/" + str(id))
    try:
        post = Post.objects.get(id=id)
        comments = Comment.objects.all().filter(post=post.id)
    except:
        post = None
        comments = []
    
    form = CommentForm()
    context = {
        "post": post,
        "form" : form,
        "comments":comments
    }
    return render(req, "post.html", context)

@not_loggedin
def register(req):
    form = UserForm()
    if req.method == "POST":
        form = UserForm(req.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password1"])
            new_user = Profile();
            new_user.user = user
            new_user.save()
            login(req, user)
            return redirect('/')
        else:  
            errors = list(form.errors.values())          
            messages.error(req, errors[0])
        return redirect('/register')
    context = {
        "form": form
    }
    return render(req, "register.html", context)

@login_required(login_url="/login")
def settings(req):
    if req.method == "POST":
        form = SettingForm(req.POST, req.FILES, instance=req.user.profile)
        if form.is_valid():
            form.save()
        else:
            messages.error(req, "Invalid Data Provided")
        return redirect('/settings')
    form = SettingForm(instance=req.user.profile)
    context = {
        "form" : form
    }
    return render(req, "settings.html", context)


def user(req, id):
    
    try:
        found_user = User.objects.get(id=id)
        userDesc = found_user.profile
        posts = Post.objects.all().filter(user=found_user.id)
        
    except:
        found_user = None
        userDesc = None
        posts = []
    
    context = {
        "fuser": found_user,
        "userDesc" : userDesc,
        "posts" : posts
        }
    return render(req, "userpage.html", context)

@login_required(login_url="/login")
def createCommunity(req):
    form = CommunityForm()
    if req.method == "POST":
        form = CommunityForm(req.POST, req.FILES)
        if form.is_valid():
            community = form.save()
            community.users.add(req.user)
            community.admins.add(req.user)
            community.save()
            return redirect('/c/' + str(community.id))
        else:
            messages.error(req, "Invalid Information !")
            return redirect('/create-community')
    context = {
        "form" : form
    }
    return render(req, "create-community.html", context)

def search(req):
    try:
        query = req.GET.get("q")
        posts = Post.objects.all().filter(Q(title__contains=query) | Q(description__contains=query))
    except:
        query = None
        posts = []
    context = {
        "posts" : posts
    }
    return render(req, "search.html", context)