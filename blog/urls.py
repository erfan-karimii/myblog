from django.urls import path
from . import views


app_name = 'blog'



urlpatterns = [
    path('',views.home, name='home'),
    path('blogs/',views.blogs, name='blogs'),
    path('about-us/',views.about_us, name='about-us'),
    path('authors/',views.authors, name='authors'),
    path('blog_detail/<id>',views.detail_blog_view, name='detail'),
    path('blog/<cat>',views.category_blog_view, name='cat'),
]