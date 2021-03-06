from django.conf.urls import url
from blog import views


urlpatterns = [
    url(r"backend/add_article/",views.add_article),
    url(r"up_down/",views.up_down),
    url(r"category/(\w+)/",views.category),
url(r'^query/', views.query),

    # /blog/xiaohei/tag/python
    # /blog/xiaohei/category/技术
    # /blog/xiaohei/archive/2018-05
    # url(r'(\w+)/tag/(\w+)', views.tag),
    # url(r'(\w+)/category/(\w+)', views.category),
    # url(r'(\w+)/archive/(.+)', views.archive),

    # 三和一 URL
    url(r'comment/', views.comment),
    url(r'comment_tree/(\d+)/', views.comment_tree),
    url(r'(\w+)/article/(\d+)/edit/$', views.edit_article_detail),  # 日记详情  article_detail(request, xiaohei, 1)
    url(r'(\w+)/article/(\d+)/delete/$', views.delete_article_detail),  # 日记详情  article_detail(request, xiaohei, 1)
    url(r'(\w+)/(tag|category|archive)/(.+)/', views.home),  # home(request, username, tag, 'python')



    url(r'(\w+)/article/(\d+)/$', views.article_detail),  # 日记详情  article_detail(request, xiaohei, 1)


    # url(r'(\w+)', views.home),  # home(request, username)

]