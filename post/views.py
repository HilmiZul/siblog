from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from post.models import Post, Page, Category
from account.models import Profile
from menus.models import *
from settings.models import General

# Create your views here.
# semua post/artikel
def posts(request):
  posts = Post.objects.filter(publish=True).order_by('-date_post')
  tag_title = General.objects.get(id=1)
  tag_title_dyn = "Semua Artikel"
  main_menus = MainMenu.objects.filter(publish=True).order_by('id')
  sub_menus = SubMenu.objects.filter(publish=True).order_by('id')
  
  paginator = Paginator(posts, 8)
  page = request.GET.get('page')
  try:
    posts = paginator.page(page)
  except PageNotAnInteger:
    posts = paginator.page(1)
  except EmptyPage:
    posts = paginator.page(paginator.num_pages)
    
  return render(request, 'posts.html', {'posts':posts, 'tag_title':tag_title, 'tag_title_dyn':tag_title_dyn, 
                                        'main_menus':main_menus, 'sub_menus':sub_menus}) 

# detil post/artikel
def detail_post(request,id_post):
  post = Post.objects.get(id=int(id_post))
  profile = Profile.objects.get(id=post.postman_id)
  tag_title = General.objects.get(id=1)
  tag_title_dyn = post.title
  main_menus = MainMenu.objects.filter(publish=True).order_by('id')
  sub_menus = SubMenu.objects.filter(publish=True).order_by('id')
  return render(request, 'detail-post.html', {'post':post, 'profile':profile, 'tag_title':tag_title, 'tag_title_dyn':tag_title_dyn, 
                                              'main_menus':main_menus, 'sub_menus':sub_menus})

# detil halaman statis (page)
def statis(request,id_page):
  statis = Page.objects.get(id=int(id_page))
  tag_title = General.objects.get(id=1)
  tag_title_dyn = statis.title
  main_menus = MainMenu.objects.filter(publish=True).order_by('id')
  sub_menus = SubMenu.objects.filter(publish=True).order_by('id')
  return render(request, 'statis.html', {'statis':statis, 'tag_title':tag_title, 'tag_title_dyn':tag_title_dyn, 
                                         'main_menus':main_menus, 'sub_menus':sub_menus})
  
# show posts in category
def categories(request,id_category):
  posts_in_cat = Post.objects.filter(publish=True, category_id=id_category).order_by('-date_post')
  get_cat = Category.objects.get(id=id_category)
  tag_title = General.objects.get(id=1)
  tag_title_dyn = get_cat.nama
  main_menus = MainMenu.objects.filter(publish=True).order_by('id')
  sub_menus = SubMenu.objects.filter(publish=True).order_by('id')
  
  paginator = Paginator(posts_in_cat, 8)
  page = request.GET.get('page')
  try:
    posts_in_cat = paginator.page(page)
  except PageNotAnInteger:
    posts_in_cat = paginator.page(1)
  except EmptyPage:
    posts_in_cat = paginator.page(paginator.num_pages)
    
  return render(request, 'category.html', {'posts_in_cat':posts_in_cat, 'get_cat':get_cat, 
                                          'tag_title':tag_title, 'tag_title_dyn':tag_title_dyn,  'main_menus':main_menus, 'sub_menus':sub_menus})
  
