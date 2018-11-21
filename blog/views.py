from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.contrib import auth
from geetest import GeetestLib
from blog import forms, models
from django.db.models import Count
import logging
from blog import trans_time

# 生成一个logger实例，专门用来记录日志
logger = logging.getLogger(__name__)
# logger_s10 = logging.getLogger("collect")

# Create your views here.

# VALID_CODE = ""


# 自己生成验证码的登录
# def login(request):
#     # if request.is_ajax():  # 如果是AJAX请求
#     if request.method == "POST":
#         # 初始化一个给AJAX返回的数据
#         ret = {"status": 0, "msg": ""}
#         # 从提交过来的数据中 取到用户名和密码
#         username = request.POST.get("username")
#         pwd = request.POST.get("password")
#         valid_code = request.POST.get("valid_code")  # 获取用户填写的验证码
#         print(valid_code)
#         print("用户输入的验证码".center(120, "="))
#         if valid_code and valid_code.upper() == request.session.get("valid_code", "").upper():
#             # 验证码正确
#             # 利用auth模块做用户名和密码的校验
#             user = auth.authenticate(username=username, password=pwd)
#             if user:
#                 # 用户名密码正确
#                 # 给用户做登录
#                 auth.login(request, user)
#                 ret["msg"] = "/index/"
#             else:
#                 # 用户名密码错误
#                 ret["status"] = 1
#                 ret["msg"] = "用户名或密码错误！"
#         else:
#             ret["status"] = 1
#             ret["msg"] = "验证码错误"
#
#         return JsonResponse(ret)
#     return render(request, "login.html")


# 使用极验滑动验证码的登录

def login(request):
    # if request.is_ajax():  # 如果是AJAX请求
    if request.method == "POST":
        # 初始化一个给AJAX返回的数据
        ret = {"status": 0, "msg": ""}
        # 从提交过来的数据中 取到用户名和密码
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        # 获取极验 滑动验证码相关的参数
        gt = GeetestLib(pc_geetest_id, pc_geetest_key)
        challenge = request.POST.get(gt.FN_CHALLENGE, '')
        validate = request.POST.get(gt.FN_VALIDATE, '')
        seccode = request.POST.get(gt.FN_SECCODE, '')
        status = request.session[gt.GT_STATUS_SESSION_KEY]
        user_id = request.session["user_id"]

        if status:
            result = gt.success_validate(challenge, validate, seccode, user_id)
        else:
            result = gt.failback_validate(challenge, validate, seccode)
        if result:
            # 验证码正确
            # 利用auth模块做用户名和密码的校验
            user = auth.authenticate(username=username, password=pwd)
            if user:
                # 用户名密码正确
                # 给用户做登录
                auth.login(request, user)  # 将登录用户赋值给 request.user
                ret["msg"] = "/index/"
            else:
                # 用户名密码错误
                ret["status"] = 1
                ret["msg"] = "用户名或密码错误！"
        else:
            ret["status"] = 1
            ret["msg"] = "验证码错误"

        return JsonResponse(ret)
    return render(request, "login3.html")


# 注销
def logout(request):
    auth.logout(request)
    return redirect("/index/")


def index(request):
    blog_count = models.Article.objects.all().count()
    from datetime import date, timedelta, datetime
    models.Index_page.objects.create(visit_num=1,visit_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S").split(" ")[0])
    # now = models.Index_page.objects.filter(visit_time=datetime.now().strftime("%Y-%m-%d")).count()
    now = datetime.now()
    now_str = now.strftime("%Y-%m-%d %H:%M:%S").split(" ")[0]
    last_week = now - timedelta(days=6)
    last_week_str = last_week.strftime("%Y-%m-%d %H:%M:%S").split(" ")[0]
    import collections
    date_count={}
    date_count = collections.OrderedDict()
    for date in trans_time.get_all_dates(last_week_str,now_str):
        date_count[date] = models.Index_page.objects.filter(visit_time=date).count()
    # print(date_count)
    charts_count={}
    charts_count = collections.OrderedDict()
    for k, v in date_count.items():
        charts_count[k]=v
    # print(charts_count)
    #绘制图表
    list1=[]
    list2=[]
    for k,v in charts_count.items():
        list1.append(k)
        list2.append(v)
    # print(list1,list2)
    #条形图
    # from pyecharts import Bar
    # bar = Bar("博客访客分析表", "一周不见居然有这么多人访问",title_color="#336699",background_color='#404a59')
    # bar.add("博客最近一周阅览人数",list1 , list2)
    # bar.render(path="static/charts/charts.png")
    #折线图
    #绘制图表
    from pyecharts import Line
    line = Line('博客访客分析表')
    line.add('最近一周博客访问量', list1, list2,
             mark_point=['average', 'max', 'min'],  # 标注点：平均值，最大值，最小值
             mark_point_symbol='arrow',  # 标注点：钻石形状
             mark_point_textcolor='#40ff27',
             mark_point_symbolsize=40)
    line.render(path="static/charts/charts.png")
    #总阅读排行
    article_query = models.Article.objects.all().order_by("-read_num")[:10]
    #24小时阅读排行
    article_list = models.Article.objects.all()
    article_dic = {}
    article_dic_list = []
    for article in article_list:
        read_count = models.Read.objects.filter(article=article,
                                                read_time=now.strftime("%Y-%m-%d %H:%M:%S").split(" ")[0]).count()
        article_dic["count"] = read_count
        article.today_read_num = read_count
        article.save()
        article_dic["title"] = article.title
        article_dic["nid"] = article.nid

        article_dic_list.append(article_dic.copy())
    # 字典排序
    sort_read_num = sorted(article_dic_list, key=lambda e: e.__getitem__('count'))
    sort_read_num.reverse()
    article_list_list = []
    for i in sort_read_num:
        nid = i["nid"]
        n = 1
        article = models.Article.objects.filter(nid=nid).first()
        article_list_list.append(article)
        n = n + 1
        if n >10:
            break
    category_list = models.Category.objects.all()
    index_visit = models.Index_page.objects.all().count()
    #文章进度条占比
    import random
    color_list = ["progress-bar-success", "progress-bar-info", "progress-bar-warning", "progress-bar-danger"]
    for category in category_list:
        category_rate = ((models.Article.objects.filter(category=category).count()) / (models.Article.objects.all().count())) * 100
        category.rate = round(category_rate, 2)
        category.save()
        category.process_color = color_list[random.randint(0,3)]


    return render(request,"index.html",{"blog_count":blog_count,"article_query":article_query,"article_list_list":article_list_list[0:10],"category_list":category_list,"index_visit":index_visit})


# 获取验证码图片的视图
def get_valid_img(request):
    # with open("valid_code.png", "rb") as f:
    #     data = f.read()
    # 自己生成一个图片
    from PIL import Image, ImageDraw, ImageFont
    import random

    # 获取随机颜色的函数
    def get_random_color():
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    # 生成一个图片对象
    img_obj = Image.new(
        'RGB',
        (220, 35),
        get_random_color()
    )
    # 在生成的图片上写字符
    # 生成一个图片画笔对象
    draw_obj = ImageDraw.Draw(img_obj)
    # 加载字体文件， 得到一个字体对象
    font_obj = ImageFont.truetype("static/font/kumo.ttf", 28)
    # 开始生成随机字符串并且写到图片上
    tmp_list = []
    for i in range(5):
        u = chr(random.randint(65, 90))  # 生成大写字母
        l = chr(random.randint(97, 122))  # 生成小写字母
        n = str(random.randint(0, 9))  # 生成数字，注意要转换成字符串类型

        tmp = random.choice([u, l, n])
        tmp_list.append(tmp)
        draw_obj.text((20+40*i, 0), tmp, fill=get_random_color(), font=font_obj)

    print("".join(tmp_list))
    print("生成的验证码".center(120, "="))
    # 不能保存到全局变量
    # global VALID_CODE
    # VALID_CODE = "".join(tmp_list)

    # 保存到session
    request.session["valid_code"] = "".join(tmp_list)
    # 加干扰线
    # width = 220  # 图片宽度（防止越界）
    # height = 35
    # for i in range(5):
    #     x1 = random.randint(0, width)
    #     x2 = random.randint(0, width)
    #     y1 = random.randint(0, height)
    #     y2 = random.randint(0, height)
    #     draw_obj.line((x1, y1, x2, y2), fill=get_random_color())
    #
    # # 加干扰点
    # for i in range(40):
    #     draw_obj.point((random.randint(0, width), random.randint(0, height)), fill=get_random_color())
    #     x = random.randint(0, width)
    #     y = random.randint(0, height)
    #     draw_obj.arc((x, y, x+4, y+4), 0, 90, fill=get_random_color())

    # 将生成的图片保存在磁盘上
    # with open("s10.png", "wb") as f:
    #     img_obj.save(f, "png")
    # # 把刚才生成的图片返回给页面
    # with open("s10.png", "rb") as f:
    #     data = f.read()

    # 不需要在硬盘上保存文件，直接在内存中加载就可以
    from io import BytesIO
    io_obj = BytesIO()
    # 将生成的图片数据保存在io对象中
    img_obj.save(io_obj, "png")
    # 从io对象里面取上一步保存的数据
    data = io_obj.getvalue()
    return HttpResponse(data)


# 请在官网申请ID使用，示例ID不可使用
pc_geetest_id = "b46d1900d0a894591916ea94ea91bd2c"
pc_geetest_key = "36fc3fe98530eea08dfc6ce76e3d24c4"


# 处理极验 获取验证码的视图
def get_geetest(request):
    user_id = 'test'
    gt = GeetestLib(pc_geetest_id, pc_geetest_key)
    status = gt.pre_process(user_id)
    request.session[gt.GT_STATUS_SESSION_KEY] = status
    request.session["user_id"] = user_id
    response_str = gt.get_response_str()
    return HttpResponse(response_str)


# 注册的视图函数
def register(request):
    if request.method == "POST":
        print(request.POST)
        print("=" * 120)
        ret = {"status": 0, "msg": ""}
        form_obj = forms.RegForm(request.POST)
        print(request.POST)
        # 帮我做校验
        if form_obj.is_valid():
            # 校验通过，去数据库创建一个新的用户
            print("前",form_obj.cleaned_data)
            avatar_img = request.FILES.get("avatar")
            print("后",form_obj.cleaned_data)
            blog_obj = models.Blog.objects.create(title=form_obj.cleaned_data["blog_title"],
                                                  site=form_obj.cleaned_data["blog_site"])

            models.UserInfo.objects.create_user(blog=blog_obj, username=form_obj.cleaned_data["username"],
                                                password=form_obj.cleaned_data["password"],
                                                email=form_obj.cleaned_data["email"],
                                                avatar=avatar_img)
            blog_obj = models.Blog.objects.filter(title=form_obj.cleaned_data["blog_title"],
                                                  site=form_obj.cleaned_data["blog_site"]).first()
            blog_obj.theme = form_obj.cleaned_data["username"] + ".css"
            blog_obj.save()
            print(form_obj.cleaned_data)
            ret["msg"] = "/login/"
            return JsonResponse(ret)
        else:
            print(form_obj.errors)
            ret["status"] = 1
            ret["msg"] = form_obj.errors
            print(ret)
            print("=" * 120)
            return JsonResponse(ret)
    # 生成一个form对象
    form_obj = forms.RegForm()
    print(form_obj.fields)
    return render(request, "register2.html", {"form_obj": form_obj})
    # return render(request, "form_test.html", {"form_obj": form_obj})


# 校验用户名是否已被注册
def check_username_exist(request):
    ret = {"status": 0, "msg": ""}
    username = request.GET.get("username")
    print(username)
    is_exist = models.UserInfo.objects.filter(username=username)
    if is_exist:
        ret["status"] = 1
        ret["msg"] = "用户名已被注册！"
    return JsonResponse(ret)


# 个人博客主页
def home(request, username, *args):
    logger.debug("home视图获取到用户名:{}".format(username))
    # 去UserInfo表里把用户对象取出来
    user = models.UserInfo.objects.filter(username=username).first()
    print(username)
    if not user:
        logger.warning("又有人访问不存在页面了...")
        return HttpResponse("404")
    # 如果用户存在需要将TA写的所有文章找出来
    blog = user.blog
    print(type(user),type(blog),type(blog.nid))
    if not args:
        logger.debug("args没有接收到参数，默认走的是用户的个人博客页面！")
        # 我的文章列表
        article_list = models.Article.objects.filter(user=user)
        # 我的文章分类及每个分类下文章数
        # 将我的文章按照我的分类分组，并统计出每个分类下面的文章数
        # category_list = models.Category.objects.filter(blog=blog)
        # category_list = models.Category.objects.filter(blog=blog).annotate(c=Count("article")).values("title", "c")
        # # [{'title': '技术', 'c': 2}, {'title': '生活', 'c': 1}, {'title': 'LOL', 'c': 1}]
        # # 统计当前站点下有哪一些标签，并且按标签统计出文章数
        # tag_list = models.Tag.objects.filter(blog=blog).annotate(c=Count("article")).values("title", "c")
        #
        # # 按日期归档
        # archive_list = models.Article.objects.filter(user=user).extra(
        #     select={"archive_ym": "date_format(create_time,'%%Y-%%m')"}
        # ).values("archive_ym").annotate(c=Count("nid")).values("archive_ym", "c")
    else:
        logger.debug(args)
        logger.debug("------------------------------")
        # 表示按照文章的分类或tag或日期归档来查询
        # args = ("category", "技术")
        # article_list = models.Article.objects.filter(user=user).filter(category__title="技术")
        if args[0] == "category":
            article_list = models.Article.objects.filter(user=user).filter(category__title=args[1])
        elif args[0] == "tag":
            article_list = models.Article.objects.filter(user=user).filter(tags__title=args[1])
        else:
            # 按照日期归档
            try:
                year, month = args[1].split("-")
                logger.debug("分割得到参数year:{}, month:{}".format(year, month))
                # logger_s10.info("得到年和月的参数啦！！！！")
                logger.debug("************************")
                article_list = models.Article.objects.filter(user=user).filter(
                    create_time__year=year, create_time__month=month
                )
            except Exception as e:
                logger.warning("请求访问的日期归档格式不正确！！！")
                logger.warning((str(e)))
                return HttpResponse("404")

    category_list = models.Category.objects.filter(blog=blog).annotate(c=Count("article")).values("title", "c")
    # 查文章标签及对应的文章数
    tag_list = models.Tag.objects.filter(blog=blog).annotate(c=Count("article")).values("title", "c")
    # 按日期归档
    archive_list = models.Article.objects.filter(user=user).extra(
        select={"archive_ym": "date_format(create_time,'%%Y-%%m')"}
    ).values("archive_ym").annotate(c=Count("nid")).values("archive_ym", "c")
    return render(request, "home.html", {
        "username": username,
        "blog": blog,
        "article_list": article_list,
        "category_list": category_list, "tag_list": tag_list, "archive_list": archive_list,
        "user":user,
    })



def get_left_menu(username):
    user = models.UserInfo.objects.filter(username=username).first()
    blog = user.blog
    category_list = models.Category.objects.filter(blog=blog).annotate(c=Count("article")).values("title", "c")
    tag_list = models.Tag.objects.filter(blog=blog).annotate(c=Count("article")).values("title", "c")
    # 按日期归档
    archive_list = models.Article.objects.filter(user=user).extra(
        select={"archive_ym": "date_format(create_time,'%%Y-%%m')"}
    ).values("archive_ym").annotate(c=Count("nid")).values("archive_ym", "c")

    return category_list, tag_list, archive_list


def article_detail(request, username, pk):
    """
    :param username: 被访问的blog的用户名
    :param pk: 访问的文章的主键id值
    :return:
    """
    print(request.user)
    user = models.UserInfo.objects.filter(username=username).first()
    if not user:
        return HttpResponse("404")
    blog = user.blog
    # 找到当前的文章
    article_obj = models.Article.objects.filter(pk=pk).first()
    models.Read.objects.create(article=article_obj)
    # if read_obj:
    #     read_obj.read_num = read_obj.read_num + 1
    #     read_obj.save()
    # else:
    #     models.Read.objects.create(article=article_obj)
    #阅读数
    article_obj.read_num = article_obj.read_num + 1
    article_obj.save()

    # 所有评论列表
    comment_list=models.Comment.objects.filter(article_id=pk)
    # 查询文章分类及对应的文章数
    category_list = models.Category.objects.filter(blog=blog).annotate(c=Count("article")).values("title", "c")
    # 查文章标签及对应的文章数
    tag_list = models.Tag.objects.filter(blog=blog).annotate(c=Count("article")).values("title", "c")

    # 按日期归档
    archive_list = models.Article.objects.filter(user=user).extra(
        select={"archive_ym": "date_format(create_time,'%%Y-%%m')"}
    ).values("archive_ym").annotate(c=Count("nid")).values("archive_ym", "c")

    return render(request,"article_detail.html",{"username": username,"article": article_obj,"blog": blog,"comment_list":comment_list,"category_list": category_list,"tag_list": tag_list,"archive_list": archive_list})


import json

from django.db.models import F

def up_down(request):
    print(request.POST)
    article_id=request.POST.get('article_id')
    is_up=json.loads(request.POST.get('is_up'))
    user=request.user
    response={"state":True}
    print("is_up",is_up)
    try:
        models.ArticleUpDown.objects.create(user=user,article_id=article_id,is_up=is_up)
        models.Article.objects.filter(pk=article_id).update(up_count=F("up_count")+1)

    except Exception as e:
        response["state"]=False
        response["fisrt_action"]=models.ArticleUpDown.objects.filter(user=user,article_id=article_id).first().is_up




    return JsonResponse(response)
    #return HttpResponse(json.dumps(response))


def comment(request):
    pid=request.POST.get("pid")
    article_id=request.POST.get("article_id")
    content=request.POST.get("content")
    user_pk=request.user.pk
    response={}
    if not pid:  #根评论
        comment_obj=models.Comment.objects.create(article_id=article_id,user_id=user_pk,content=content)
    else:
        comment_obj=models.Comment.objects.create(article_id=article_id,user_id=user_pk,content=content,parent_comment_id=pid)
    response["create_time"]=comment_obj.create_time.strftime("%Y-%m-%d")
    response["content"]=comment_obj.content
    response["username"]=comment_obj.user.username

    return JsonResponse(response)


def comment_tree(request,article_id):

    ret=list(models.Comment.objects.filter(article_id=article_id).values("pk","content","parent_comment_id"))
    print(ret)
    return JsonResponse(ret,safe=False)


def search_article(request):
    # index_page_obj = models.Index_page.objects.filter(id=1).first()
    # index_page_obj.visit_num = index_page_obj.visit_num + 1
    # index_page_obj.save()
    # index_visit = index_page_obj.visit_num
    s_article = request.POST.get("search_article_name", None)
    from django.db.models import Q
    import operator
    from functools import reduce
    page_num = request.GET.get("page")
    print(page_num)
    try:
        keys = s_article.split(' ')
    except Exception as e:
        keys = s_article
    condition = reduce(operator.and_, (Q(title__icontains=x) for x in keys))
    # total_count = models.Article.objects.filter(title__icontains=s_article).count()
    total_count = models.Article.objects.filter(condition).count()
    from utils.mypage import Page
    page_obj = Page(page_num, total_count, per_page=10, max_page=11, url_prefix="/search_article/")
    page_html = page_obj.page_html()

    category_list = []
    import random
    color_list = ["label-primary", "label-success", "label-info", "label-warning","label-danger"]
    for blog in models.Blog.objects.all():
        category = models.Category.objects.filter(blog=blog).annotate(c=Count("article")).values("title", "c","blog","category_color")
        category.blog=blog
        user = models.UserInfo.objects.filter(blog=category.blog).first()
        category.user=user
        category.category_color = color_list[random.randint(0, 4)]
        # print(category.user)
        category_list.extend(category)
    # print(category_list)
    category_list_checkbox = models.Category.objects.all()
    print(category_list)
    article_list_all = models.Article.objects.all()
    article_random = []
    import random
    for i in range(10):
        article_random_one = article_list_all[random.randint(0, len(article_list_all)-1)]
        if article_random_one not in article_random:
            article_random.append(article_random_one)

    #今日阅读排行
    from datetime import date, timedelta, datetime
    now = datetime.now()
    article_list = models.Article.objects.all()
    article_dic = {}
    article_dic_list = []
    for article in article_list:
        read_count = models.Read.objects.filter(article=article,
                                                read_time=now.strftime("%Y-%m-%d %H:%M:%S").split(" ")[0]).count()
        article_dic["count"] = read_count
        article.today_read_num = read_count
        article.save()
        article_dic["title"] = article.title
        article_dic["nid"] = article.nid

        article_dic_list.append(article_dic.copy())
    # 字典排序
    sort_read_num = sorted(article_dic_list, key=lambda e: e.__getitem__('count'))
    sort_read_num.reverse()
    article_list_list = []
    n = 0
    for i in sort_read_num:
        nid = i["nid"]
        article = models.Article.objects.filter(nid=nid).first()
        article_list_list.append(article)
        n = n + 1
        if n == 10:
            break
        print(n)
    print(article_list_list[0:11])
    index_visit = models.Index_page.objects.all().count()
    article_count = models.Article.objects.all().count()
    print(s_article)
    if s_article == None:
        article_list_page = models.Article.objects.all()[page_obj.start:page_obj.end]
    else:
        # article_list = models.Article.objects.filter(title__icontains=s_article)[page_obj.start:page_obj.end]
        article_list_page = models.Article.objects.filter(condition)[page_obj.start:page_obj.end]
    return render(request, "blog.html", {"article_list": article_list,"page_html":page_html,"category_list":category_list,"category_list_checkbox":category_list_checkbox,"article_random":article_random,"article_list_list":article_list_list[0:10],"index_visit":index_visit,"article_list_page":article_list_page,"article_count":article_count,"s_article":s_article})

from bs4 import BeautifulSoup
def add_article(request):
    if request.user:
        if request.method == "POST":
            title = request.POST.get("title")
            category = request.POST.get("category")
            print(category)
            article_content = request.POST.get("article_content")
            user = request.user
            print(user,type(user),user.username)
            username = user.username
            user = models.UserInfo.objects.filter(username=username).first()
            # if not models.Blog.objects.filter(userinfo=user).first():
            #     blog_name = user.username + "的博客"
            #     blog_theme = user.username + "的css"
            #     blog_site = user.username
            #     models.Blog.objects.create(title=blog_name,theme=blog_theme)
            blog = user.blog
            print(type(blog))
            print(user, type(user),type(blog), user.username)
            if not models.Category.objects.filter(title=category):
                models.Category.objects.create(title=category,blog_id=blog.nid)
            bs = BeautifulSoup(article_content,"html.parser")
            print(3)
            print(str(bs.text)[0:150])
            desc = str(bs.text)[0:150]+"..."
            print(1)
            category_obj = models.Category.objects.filter(title=category).first()
            article_obj = models.Article.objects.create(user=user,category=category_obj,title=title,desc=desc)
            print(2)
            models.ArticleDetail.objects.create(content=article_content,article=article_obj)
            return redirect("/blog/"+ username + "/")
        return render(request,"add_article.html")
    else:
        return redirect("/login/")

from my_blogs import settings
import os,json
def upload(request):
    obj = request.FILES.get("imgFile")
    path = os.path.join(settings.MEDIA_ROOT,"add_article_img",obj.name)
    with open(path,"wb") as f:
        for line in obj:
            f.write(line)

    res={
        "error":0,
        "url":"/media/add_article_img/"+obj.name
    }

    return HttpResponse(json.dumps(res))

def register2(request):
    if request.method == "POST":
        print(request.POST)
        print("=" * 120)
        ret = {"status": 0, "msg": ""}
        form_obj = forms.RegForm(request.POST)
        print(request.POST)
        # 帮我做校验
        if form_obj.is_valid():

            # 校验通过，去数据库创建一个新的用户
            form_obj.cleaned_data.pop("re_password")
            avatar_img = request.FILES.get("avatar")
            models.UserInfo.objects.create_user(**form_obj.cleaned_data, avatar=avatar_img)
            ret["msg"] = "/index/"
            return JsonResponse(ret)
        else:
            print(form_obj.errors)
            ret["status"] = 1
            ret["msg"] = form_obj.errors
            print(ret)
            print("=" * 120)
            return JsonResponse(ret)
    # 生成一个form对象
    form_obj = forms.RegForm()
    print(form_obj.fields)
    return render(request, "register2.html", {"form_obj": form_obj})
    # return render(request, "form_test.html", {"form_obj": form_obj})

def login3(request):
    # if request.is_ajax():  # 如果是AJAX请求
    if request.method == "POST":
        # 初始化一个给AJAX返回的数据
        ret = {"status": 0, "msg": ""}
        # 从提交过来的数据中 取到用户名和密码
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        # 获取极验 滑动验证码相关的参数
        gt = GeetestLib(pc_geetest_id, pc_geetest_key)
        challenge = request.POST.get(gt.FN_CHALLENGE, '')
        validate = request.POST.get(gt.FN_VALIDATE, '')
        seccode = request.POST.get(gt.FN_SECCODE, '')
        status = request.session[gt.GT_STATUS_SESSION_KEY]
        user_id = request.session["user_id"]

        if status:
            result = gt.success_validate(challenge, validate, seccode, user_id)
        else:
            result = gt.failback_validate(challenge, validate, seccode)
        if result:
            # 验证码正确
            # 利用auth模块做用户名和密码的校验
            user = auth.authenticate(username=username, password=pwd)
            if user:
                # 用户名密码正确
                # 给用户做登录
                auth.login(request, user)  # 将登录用户赋值给 request.user
                ret["msg"] = "/index/"
            else:
                # 用户名密码错误
                ret["status"] = 1
                ret["msg"] = "用户名或密码错误！"
        else:
            ret["status"] = 1
            ret["msg"] = "验证码错误"

        return JsonResponse(ret)
    return render(request, "login3.html")

def blog(request):
    # 查询所有的文章列表
    # article_list = models.Article.objects.all()
    # index_page_obj = models.Index_page.objects.filter(id=1).first()
    # index_page_obj.visit_num = index_page_obj.visit_num + 1
    # index_page_obj.save()
    # index_visit = index_page_obj.visit_num

    page_num = request.GET.get("page")
    print(page_num)
    total_count = models.Article.objects.all().count()
    from utils.mypage import Page
    page_obj = Page(page_num, total_count, per_page=7, max_page=11, url_prefix="/blog/")
    article_list_page = models.Article.objects.all()[page_obj.start:page_obj.end]
    page_html = page_obj.page_html()

    category_list = []
    import random
    color_list = ["label-primary", "label-success", "label-info", "label-warning","label-danger"]
    for blog in models.Blog.objects.all():
        category = models.Category.objects.filter(blog=blog).annotate(c=Count("article")).values("title", "c","blog","category_color")
        category.blog=blog
        user = models.UserInfo.objects.filter(blog=category.blog).first()
        category.user=user
        category.category_color = color_list[random.randint(0, 4)]
        # print(category.user)
        category_list.extend(category)
    # print(category_list)
    category_list_checkbox = models.Category.objects.all()
    print(category_list)
    article_list_all = models.Article.objects.all()
    article_random = []
    article_random_2 = []
    import random
    for i in range(10):
        article_random_one = article_list_all[random.randint(0, len(article_list_all)-1)]
        if article_random_one not in article_random:
            article_random.append(article_random_one)
        article_random_two = article_list_all[random.randint(0, len(article_list_all) - 1)]
        if article_random_two not in article_random:
            article_random_2.append(article_random_two)

    #今日阅读排行
    from datetime import date, timedelta, datetime
    now = datetime.now()
    article_list = models.Article.objects.all()
    article_dic = {}
    article_dic_list = []
    for article in article_list:
        read_count = models.Read.objects.filter(article=article,
                                                read_time=now.strftime("%Y-%m-%d %H:%M:%S").split(" ")[0]).count()
        article_dic["count"] = read_count
        article.today_read_num = read_count
        article.save()
        article_dic["title"] = article.title
        article_dic["nid"] = article.nid

        article_dic_list.append(article_dic.copy())
    # 字典排序
    sort_read_num = sorted(article_dic_list, key=lambda e: e.__getitem__('count'))
    sort_read_num.reverse()
    article_list_list = []
    n = 0
    for i in sort_read_num:
        nid = i["nid"]
        article = models.Article.objects.filter(nid=nid).first()
        article_list_list.append(article)
        n = n + 1
        if n == 10:
            break
        print(n)
    print(article_list_list[0:10])
    index_visit = models.Index_page.objects.all().count()
    article_count = models.Article.objects.all().count()
    # import random
    # category_list_all = models.Category.objects.all()
    # color_list = ["label-primary", "label-success", "label-info", "label-warning","label-danger"]
    # for category in category_list:
    #     category.category_color = color_list[random.randint(0,4)]
    #     print(category.category_color)
    #     category.save()

    return render(request, "blog.html", {"article_list": article_list,"page_html":page_html,"category_list":category_list,"category_list_checkbox":category_list_checkbox,"article_random":article_random,"article_list_list":article_list_list[0:10],"index_visit":index_visit,"article_list_page":article_list_page,"article_count":article_count,"article_random_2":article_random_2})

def category(request,category):
    page_num = request.GET.get("page")
    print(page_num)
    total_count = models.Article.objects.filter(category__title=category).count()
    from utils.mypage import Page
    page_obj = Page(page_num, total_count, per_page=7, max_page=10, url_prefix="/blog/category/" + str(category) + "/")
    article_list = models.Article.objects.filter(category__title=category)[page_obj.start:page_obj.end]
    print(article_list)
    page_html = page_obj.page_html()

    category_list = models.Category.objects.all()
    article_count = models.Article.objects.all().count()
    from datetime import date, timedelta, datetime
    now = datetime.now()

    article_list_all = models.Article.objects.all()
    article_list_category = models.Article.objects.filter(category__title=category)
    article_dic = {}
    article_dic_list = []
    for article in article_list_category:
        read_count = models.Read.objects.filter(article=article,
                                                read_time=now.strftime("%Y-%m-%d %H:%M:%S").split(" ")[0]).count()
        article_dic["count"] = read_count
        article.category_read_num = read_count
        article.save()
        article_dic["title"] = article.title
        article_dic["nid"] = article.nid
        article_dic_list.append(article_dic.copy())
    # 字典排序
    sort_read_num = sorted(article_dic_list, key=lambda e: e.__getitem__('count'))
    sort_read_num.reverse()
    article_list_list = []
    for i in sort_read_num:
        nid = i["nid"]
        n = 1
        article = models.Article.objects.filter(nid=nid).first()
        article_list_list.append(article)
        n = n + 1
        if n > 10:
            break
    article_random = []
    import random
    for i in range(10):
        article_random_one = article_list_all[random.randint(0, len(article_list_all)-1)]
        if article_random_one not in article_random:
            article_random.append(article_random_one)
    category_choice=category


    return render(request,"category.html",{"article_list": article_list,"page_html":page_html,"category_list":category_list,"article_count":article_count,"article_list_list":article_list_list,"article_random":article_random,"category_choice":category_choice})

def query(request):
    return render(request,'query.html')

