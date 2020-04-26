from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView

from .models import BlogArticle
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger, PaginationMixin
import markdown
from markdown.extensions import extra,codehilite,toc



# Create your views here.

# class ArticleListView():
class ArticleListView(PaginationMixin, ListView):
    model = BlogArticle
    template_name = 'blog/article_list.html'
    context_object_name = 'blogs'
    paginate_by = 10

# def article_list(request):
#     get_blogs = BlogArticle.objects.all()
#     try:
#         page = request.GET.get('page', 1)
#     except PageNotAnInteger:
#         page = 1
#     p = Paginator(get_blogs, per_page=10, request=request)
#     blogs = p.page(page)
#     return render(request,"blog/article_list.html", {"blogs":blogs})



def detail(request, blog_id):

    blog = get_object_or_404(BlogArticle, id=blog_id)
    blog.increase_views()
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    blog.body = md.convert(blog.body)
    blog.toc = md.toc
    return render(request, "blog/detail.html", context={"blog": blog},)

def page_not_found(request):
    return render(request,'404.html')