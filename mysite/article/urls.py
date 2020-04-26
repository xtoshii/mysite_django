from django.urls import path,include
from . import views
from django.conf.urls import handler404


app_name = "article"

urlpatterns = [
    path('',views.ArticleListView.as_view(), name='ArticleListView'),
    path('<int:blog_id>/',views.detail,name='detail'),
]
