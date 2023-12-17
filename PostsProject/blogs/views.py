from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import BlogPost, Comment, Rating
from .forms import BlogPostForm, CommentForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Avg
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm
from django.db.utils import IntegrityError



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Welcome back, {}!'.format(user.username))
                return redirect('post_list')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            messages.success(request, 'Welcome to Blog App, {}!'.format(user.username))
            return redirect('user_login')
        else:
            # Display error messages if the form is not valid
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out. See you soon!')
    return redirect('user_login')

@login_required
def post_list(request):
    posts = BlogPost.objects.all()
    paginator = Paginator(posts, 5)  # Show 5 posts per page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'post_list.html', {'posts': posts})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = BlogPostForm()
    return render(request, 'post_form.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'post_form.html', {'form': form})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    post.delete()
    return redirect('post_list')

def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = BlogPost.objects.filter(author=user)
    return render(request, 'user_profile.html', {'user_profile': user, 'posts': posts})

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_list')
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})


@login_required
def share_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    
    # Example sharing URLs (you might need to customize these)
    facebook_share_url = f'https://www.facebook.com/sharer/sharer.php?u={request.build_absolute_uri(post.get_absolute_url())}'
    twitter_share_url = f'https://twitter.com/intent/tweet?url={request.build_absolute_uri(post.get_absolute_url())}&text={post.title}'

    return render(request, 'share_post.html', {'post': post, 'facebook_share_url': facebook_share_url, 'twitter_share_url': twitter_share_url})

@login_required

def rate_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    
    if request.method == 'POST':
        rating_value = None
        if 'rating' in request.POST:
            rating_value = int(request.POST.get('rating'))
        elif 'direct_input' in request.POST:
            rating_value = int(request.POST.get('direct_input'))

        if 1 <= rating_value <= 5:
            try:
                user_rating, created = Rating.objects.get_or_create(post=post, user=request.user, defaults={'value': rating_value})
                if not created:
                    user_rating.value = rating_value
                    user_rating.save()
                messages.success(request, 'Thank you for rating!')
                return redirect('post_list')
            except IntegrityError:
                messages.error(request, 'Error occurred while saving the rating.')
        else:
            messages.error(request, 'Invalid rating. Please provide a valid rating value between 1 and 5.')

    return render(request, 'rate_post.html', {'post': post})
@login_required
def blog_post_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog_post_detail.html', {'post': post})

