from django.shortcuts import render,get_object_or_404
from .models import Project_blog

def all_blogs(request):
    #Instead of showing all we can limit the objects like this
    #I created 6 models in admin page but i wanna show only 5
    projects2=Project_blog.objects.order_by('-date') [:5]
    return render(request,'blog/all_blogs.html',{'projects2':projects2})
def nextpage(request):
    projects=Project_blog.objects.order_by('-date') [5::]
    return render(request,'blog/nextpage.html',{'projects':projects})
def detail(request,blog_id):
    blog=get_object_or_404(Project_blog,pk=blog_id)
    return render(request,'blog/detail.html',{'blog':blog})
    
