from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

from .forms import PostForm
from .models import Post

# class HomePageView(ListView):
#     model = Post
#     template_name = 'home.html'

def home(request):
    posts = Post.objects.all().order_by('pk')
    context = {"posts":posts}
    return render(request, 'home.html', context)
# class CreatePostView(CreateView):
#     model = Post
#     form_class = PostForm
#     template_name = 'post.html'
#     success_url = reverse_lazy('home')

# def create(request):
#     form = PostForm(request.POST)
#     if form.is_valid():
#         form.save()
#         return HttpResponse('home.html', {'form': form})
#     else:
#         return render(request, 'post.html', {'form': form})
#

def create(request):
    form = PostForm(request.POST)
    if request.method == "POST":
        #form = MyForm(request.POST)
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            # <process form cleaned data>
            return redirect('home.html')
    else:
        return render(request, 'post.html', { 'form' : form})