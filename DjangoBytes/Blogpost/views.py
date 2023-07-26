from django.views import generic
from .models import Post
from .forms import NewUserForm,search_form,commentForm

from django.contrib.auth import login,authenticate
from django.contrib import auth
from django.contrib import messages
from django.shortcuts import  render, redirect,get_object_or_404
from django.contrib.auth.models import User
from pytube import Youtube 
from pytube import YouTube


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

def PostDetail(request, slug):
    
    template_name = 'post_detail.html'
    post=get_object_or_404(Post, slug=slug)
    comments=post.comments.filter(active=True)

    new_comment=None
    comment_form = commentForm() 
    if request.method == 'POST':
        comment_form = commentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = commentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})







def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists.")
                return redirect("register")
                
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        else:
            print(form.errors)
            messages.info(request, "Validation error.")
    else:
        form = NewUserForm()
    
    return render(request=request, template_name="register.html", context={"form": form, "messages": messages.get_messages(request)})


def search_view(request):
        form2=search_form(request.GET)
  
        results=[]
        if form2.is_valid():
            search1=form2.cleaned_data.get("search1")
            results = Post.objects.filter(title__icontains=search1)
        return render(request, "search.html", {"form2": form2, 'results': results})



def login(request):
    if request.method=='POST':
        username=request.Post['username']
        password=request.Post['password']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request, 'invalid credentials')
            return redirect("login")
    else:
        return render(request, 'login.html')
def logout(request):
    auth.logout(request)
    return redirect('logged out')


#function for social media integration
def social_integration(request):
    return render(request, 'social_integration.html')



def downloader(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        video = YouTube(url)
        title = video.title
        stream_list = video.streams.filter(progressive=True)
        context = {
            'title': title,
            'stream_list': stream_list
        }
        return render(request, 'downloader.html', context)
    return render(request, 'downloader.html',{})