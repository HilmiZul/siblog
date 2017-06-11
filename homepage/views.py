from django.shortcuts import render

from post.models import Post
from menus.models import MainMenu, SubMenu
from settings.models import General

# Create your views here.
def index(request):
  posts_in_index = Post.objects.filter(publish=True).order_by('-date_post')[:8]   # belum dilimit
  tag_title = General.objects.get(id=1)
  main_menus = MainMenu.objects.filter(publish=True).order_by('id')
  sub_menus = SubMenu.objects.filter(publish=True).order_by('id')
  return render(request, 'home.html', {'posts_in_index':posts_in_index,'tag_title':tag_title,
                                       'main_menus':main_menus, 'sub_menus':sub_menus})
