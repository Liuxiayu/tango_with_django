from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class UserInfo(AbstractUser):
    """
    用户信息表
    """
    nid = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=11, null=True, unique=True)
    avatar = models.FileField(upload_to="avatars/", default="avatars/default.png", verbose_name="头像")
    create_time = models.DateTimeField(auto_now_add=True)

    blog = models.OneToOneField(to="Blog", to_field="nid", null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name


class Blog(models.Model):
    """
    博客信息
    """
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)  # 个人博客标题
    site = models.CharField(max_length=32, unique=True,null=True)  # 个人博客后缀
    theme = models.CharField(max_length=32,null=True)  # 博客主题

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "blog站点"
        verbose_name_plural = verbose_name


class Category(models.Model):
    """
    博客日记分类
    """
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)  # 分类标题
    blog = models.ForeignKey(to="Blog", to_field="nid",on_delete=models.CASCADE)  # 外键关联博客，一个博客站点可以有多个分类
    rate = models.DecimalField( max_digits=4,decimal_places=2,null=True)
    process_color = models.CharField(max_length=32,null=True)
    category_color = models.CharField(max_length=32,null=True,default="label-primary")
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "日记分类"
        verbose_name_plural = verbose_name


class Tag(models.Model):
    """
    标签
    """
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)  # 标签名
    blog = models.ForeignKey(to="Blog", to_field="nid",on_delete=models.CASCADE)  # 所属博客

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name


class Article(models.Model):
    """
    日记
    """
    nid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, verbose_name="日记标题")  # 日记标题
    desc = models.CharField(max_length=255)  # 日记描述
    create_time = models.DateTimeField(auto_now_add=True)  # 创建时间

    # 评论数
    comment_count = models.IntegerField(verbose_name="评论数", default=0)
    # 点赞数
    up_count = models.IntegerField(verbose_name="点赞数", default=0)
    # 踩
    down_count = models.IntegerField(verbose_name="踩数", default=0)
    #阅读数
    read_num = models.IntegerField(verbose_name="阅读数", default=0)
    today_read_num = models.IntegerField(verbose_name="今日阅读数", default=0)
    category_read_num = models.IntegerField(verbose_name="分类阅读数",default=0)
    category = models.ForeignKey(to="Category", to_field="nid", null=True,on_delete=models.CASCADE)
    user = models.ForeignKey(to="UserInfo", to_field="nid",on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField(  # 中介模型
        to="Tag",
        through="Article2Tag",
        through_fields=("article", "tag"),  # 注意顺序！！！
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "日记"
        verbose_name_plural = verbose_name


class Read(models.Model):
    nid = models.AutoField(primary_key=True)
    read_num = models.IntegerField(verbose_name="浏览量", default=1)
    read_time = models.DateField(verbose_name="阅读量",auto_now_add=True)

    article = models.ForeignKey(to="Article", to_field="nid", on_delete=models.CASCADE,related_name="test")

class ArticleDetail(models.Model):
    """
    日记详情表
    """
    nid = models.AutoField(primary_key=True)
    content = models.TextField()
    article = models.OneToOneField(to="Article", to_field="nid",on_delete=models.CASCADE)

    class Meta:
        verbose_name = "日记详情"
        verbose_name_plural = verbose_name


class Article2Tag(models.Model):
    """
    日记和标签的多对多关系表
    """
    nid = models.AutoField(primary_key=True)
    article = models.ForeignKey(to="Article", to_field="nid",on_delete=models.CASCADE)
    tag = models.ForeignKey(to="Tag", to_field="nid",on_delete=models.CASCADE)

    def __str__(self):
        return "{}-{}".format(self.article.title,self.tag.title)

    class Meta:
        unique_together = (("article", "tag"),)
        verbose_name = "日记-标签"
        verbose_name_plural = verbose_name



class ArticleUpDown(models.Model):
    """
    点赞表
    """
    nid = models.AutoField(primary_key=True)
    user = models.ForeignKey(to="UserInfo", null=True,on_delete=models.CASCADE)
    article = models.ForeignKey(to="Article", null=True,on_delete=models.CASCADE)
    is_up = models.BooleanField(default=True)

    class Meta:
        unique_together = (("article", "user"),)
        verbose_name = "日记点赞"
        verbose_name_plural = verbose_name


class Comment(models.Model):
    """
    评论表
    """
    nid = models.AutoField(primary_key=True)
    article = models.ForeignKey(to="Article", to_field="nid",on_delete=models.CASCADE)
    user = models.ForeignKey(to="UserInfo", to_field="nid",on_delete=models.CASCADE)
    content = models.CharField(max_length=255)  # 评论内容
    create_time = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey("self", null=True, blank=True,on_delete=models.CASCADE)  # blank=True 在django admin里面可以不填

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name


class Index_page(models.Model):
    nid = models.AutoField(primary_key=True)
    visit_num = models.IntegerField(verbose_name="浏览量", default=0)
    visit_time = models.DateField(auto_now_add=True,null=True)