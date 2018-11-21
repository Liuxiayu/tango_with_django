import os

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_blogs.settings')
    import django
    django.setup()
    from blog import models
    form_obj = {"title":"aaaaaa","site":"bbbbb","theme":"ccccc.css"}
    # blog_obj = models.Blog.objects.create(title=form_obj["title"],
    #                                       site=form_obj["site"], theme=form_obj["theme"])
    # print(blog_obj)
    # models.UserInfo.objects.create_user(blog=blog_obj, username="sssdsdssd1s",
    #                                     password="asd1123",
    #                                     email="678313@qq.com")
    blog_obj = models.Blog.objects.filter(title="zhenghuiting11",
                                          site="zhenghuiting11").first()
    blog_obj.theme = "zhenghuiting11" + ".css"
    blog_obj.save()
    # article_list_all = models.Article.objects.all()
    # article_random = []
    # import random
    # for i in range(10):
    #     article_random.append(article_list_all[random.randint(0, len(article_list_all)-1)])
    # for article in article_list_all:

    # category_list = models.Category.objects.all()
    # print(category_list)
    # for category in category_list:
    #     print(category.title)
    #     print(category.article_set.count())
    # title = "技术"
    # article_list = models.Article.objects.filter(category__title=title)
    # print(article_list)
    # from datetime import date, timedelta, datetime
    # now = datetime.now()
    # article_obj = models.Article.objects.filter(pk=1).first()
    # # read_obj = models.Read.objects.filter(article=article_obj_read).all().first()
    # # read_obj = models.Article.objects.get(nid=1).test.all()
    # # models.Read.objects.create(article=article_obj)
    # import collections
    # article_list = models.Article.objects.all()
    # article_dic = {}
    # article_dic_list = []
    # for article in article_list:
    #
    #     read_count= models.Read.objects.filter(article=article, read_time=now.strftime("%Y-%m-%d %H:%M:%S").split(" ")[0]).count()
    #     article_dic["count"] = read_count
    #     article_dic["title"] = article.title
    #     article.today_read_num = read_count
    #     article.save()
    #     article_dic["nid"] = article.nid
    #     article_dic_list.append(article_dic.copy())
    #     print(article.today_read_num)
    # #字典排序
    # sort_read_num = sorted(article_dic_list, key=lambda e: e.__getitem__('count'))
    # sort_read_num.reverse()
    # print(sort_read_num)
    # article_list_list = []
    # for i in sort_read_num:
    #     nid = i["nid"]
    #     n = 1
    #     article = models.Article.objects.filter(nid=nid).first()
    #     article_list_list.append(article)
    #     n = n + 1
    #     if n >=10:
    #         break
    # print(article_list_list)
    import operator

    # print(article_dic,article_dic_big)

    # article_query = models.Article.objects.all().order_by("-read_num")[:7]


    # print(article_query)
    #
    # # for article in article_query[0,7]:
    # #     article_list.append(article)
    # # print(article_list)
    # for article in article_query:
    #     print(article.title)
    #     print(article.read_num)
    #     print(article.user.username)
        #子查询
    # a1 = models.Article.objects.first()
    # print(a1.user.avatar,type(a1.user))
    # article_list = models.Article.objects.all()
    # print(article_list)
    # for article in article_list:
    #     print(article,type(article))
    #     print(article.user,type(article.user))
    #     print(article.user.avatar)
    #
    #
    # #列表查询
    # # a2 = models.Article.objects.filter(pk=1)
    # # print(a2.values("user__avatar"))
    #
    # ret = models.UserInfo.objects.all().extra(
    #     select={"gt":"nid > 2"}
    # )
    # for i in ret:
    #     print(i.nid,i.gt)
    # from django.db.models import Count
    # category_list = []
    # for blog in models.Blog.objects.all():
    #     category = models.Category.objects.filter(blog=blog).annotate(c=Count("article")).values("title", "c","blog")
    #     category.blog=blog
    #     user = models.UserInfo.objects.filter(blog=category.blog).first()
    #     category.user=user
    #     username=user.username
    #     print(category)
    #     print(username)
    #     category_list.extend(category)
