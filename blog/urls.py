from django.urls import path

from blog import views
from blog.views import IndexPage, PostView, ContactView
# , PostDetailView

urlpatterns = [
    path('', views.IndexPage, name = 'home'),
    path('about/', views.PostView, name='about'),
    # path('about/<int:id>', views.PostDetailView, name='abouts'),
    path('contact/', views.ContactView, name='contact'),
    # path('/about/', BlogAbout.as_view(), name='about'),
]