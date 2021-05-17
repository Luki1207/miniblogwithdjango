from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from blog.models import Post,Comment
from blog.forms import PostForm,CommentForm
from django.urls import reverse_lazy 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView,CreateView,UpdateView,DeleteView
from .filters import UserFilter
from django.conf import settings


    
# Create your views here.


# class TableListView(ListView):
#     model                   = Post
#     template_name           = "admin/simple.html"
#     context_object_name     = 'table_artikel'
    # filter_backends     = (PostFilters)
    # search_fileds       = ('title','author','category') 


class ManageArtikelListView(LoginRequiredMixin,ListView):
    login_url           = settings.LOGIN_URL
    model               = Post
    context_object_name = 'manage_artikel'
    template_name       = "blog/manage_artikel.html"
    ordering            = ['-published_date']


    def get_queryset(self):
        query = self.request.GET.get('title_contains')
        if query:
            object_list = self.model.objects.filter(title__icontains=query)
        else:
            object_list = self.model.objects.all()
        return object_list

class AboutView(TemplateView):
    template_name = "blog/about.html"
    

class PostListView(ListView):
    model = Post
    context_object_name = 'post_list'
    
    
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    paginate_by = 3

class LpmListView(ListView):
    model = Post
    context_object_name = 'lpm_list'
    template_name = "blog/lpm_list.html"

    def get_queryset(self):
        return Post.objects.filter(category=('LPM'),published_date__lte=timezone.now()).order_by('-published_date')
    paginate_by = 3

class NgaduBakoListView(ListView):
    model = Post
    context_object_name = 'ngadu_list'
    template_name = "blog/ngadu_list.html"
    paginate_by = 3
    
    def get_queryset(self):
        return Post.objects.filter(category=('NgaduBako'),published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post

class EditorCreateView(LoginRequiredMixin,CreateView):
    model                   = Post
    form_class              = PostForm
    template_name           = 'admin/editors.html'
    success_url             = reverse_lazy('adminlte')


class CreatePostView(LoginRequiredMixin,CreateView):
    login_url               = settings.LOGIN_URL
    redirect_field_name     = 'blog/post_detail.html'
    form_class              = PostForm
    model                   = Post

class PostUpdateView(LoginRequiredMixin,UpdateView):

    login_url               = settings.LOGIN_URL
    success_url = reverse_lazy('manage_artikel')
    # redirect_field_name     = 'blog/manage_artikel.html'
    form_class              = PostForm
    model                   = Post
    
class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('manage_artikel')
    
class DraftListView(ListView):
    login_url               = settings.LOGIN_URL
    redirect_field_name     = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')
    
###############################################################################################
###############################################################################################

@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('manage_artikel')
    # ('post_detail',pk=pk)

def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = CommentForm()
    return render(request,'blog/comment_form.html', {'form':form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete() 
    return redirect('post_detail', pk=post_pk)