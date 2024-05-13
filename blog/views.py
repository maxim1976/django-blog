from django.shortcuts import render
from blog.models import Post, Category, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, EditPostForm


class BlogIndex(ListView):
    model = Post
    queryset = Post.objects.filter(is_published=True).order_by("-created_on")
    template_name = "blog/index.html"
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["featured_post"] = Post.objects.filter(is_featured=True).first()
        context["main_article"] = Post.objects.filter(is_first=True).first()
        context["categories"] = Category.objects.all()
        return context

    
class BlogCategory(ListView):
    template_name = "blog/category.html"
    context_object_name = "posts"

    def get_queryset(self):
        self.category = Category.objects.get(name=self.kwargs["category"])
        return Post.objects.filter(categories=self.category, is_published=True).order_by("-created_on")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        return context

class BlogDetail(DetailView):
    model = Post
    template_name = "blog/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.filter(post=self.get_object())
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/add_post.html"
    

class FeaturedDetailView(ListView):
    template_name = "blog/featured_detail.html"    
    queryset = Post.objects.filter(is_featured=True).order_by("-created_on")
    paginate_by = 1


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = "blog/update.html"


class DeletePostView(DeleteView):
    model = Post
    template_name = "blog/delete_post.html"
    success_url = "/"