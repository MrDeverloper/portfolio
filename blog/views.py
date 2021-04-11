from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from blog.models import Post

# class IndexPage(TemplateView):
def IndexPage(request):        
    posts = Post.objects.all()
    template_name = 'home.html'
    context = {
        'posts': posts
        }
    return render(request, 'home.html', context)
    


def PostView(request):
    template_name = "about.html"
    return render(request, template_name)

# def PostDetailView(request):
#     template_name = "about.html"
#     return render(request, template_name)

def ContactView(request):
    template_name = "contact.html"
    return render(request, template_name)








# # from django.views.generic import ListView
# from .models import Post
# # Create your views here.

# # class BlogListView(ListView):
# #     model = Post
# #     template_name = 'home.html'

# def home(request):
#     return render(request, 'templates/home.html')

# # def post(request):
#     # return render(request, 'templates/post.html', )


# # class BlogAbout(ListView):
# #     model = Post
# #     template_name = 'about.html'
    