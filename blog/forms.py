"""
bbs用到的form类
"""

from django import forms
from django.core.exceptions import ValidationError
from blog import models
# 定义一个注册的form类
class RegForm(forms.Form):
    username = forms.CharField(
        max_length=16,
        label="用户名",
        error_messages={
            "max_length": "用户名最长16位",
            "required": "用户名不能为空哦",
        },
        widget=forms.widgets.TextInput(
            attrs={"class": "form-control"},
        )
    )

    password = forms.CharField(
        min_length=6,
        label="密码",
        widget=forms.widgets.PasswordInput(
            attrs={"class": "form-control"},
            render_value=True,
        ),
        error_messages={
            "min_length": "密码至少要6位！",
            "required": "密码不能为空哦",
        }
    )

    re_password = forms.CharField(
        min_length=6,
        label="确认密码",
        widget=forms.widgets.PasswordInput(
            attrs={"class": "form-control"},
            render_value=True,
        ),
        error_messages={
            "min_length": "确认密码至少要6位！",
            "required": "确认密码不能为空哦",
        }
    )

    email = forms.EmailField(
        label="邮箱",
        widget=forms.widgets.EmailInput(
            attrs={"class": "form-control"},

        ),
        error_messages={
            "invalid": "邮箱格式不正确！",
            "required": "邮箱不能为空哦",
        }
    )

    blog_title = forms.CharField(
        max_length=32,
        label="博客标题",
        widget=forms.widgets.TextInput(
            attrs={"class": "form-control"},
        ),
        error_messages={
            "invalid": "博客标题格式不正确！",
            "required": "博客标题不能为空哦",
        }
    )

    blog_site = forms.CharField(
        max_length=32,
        label="博客站点",
        widget=forms.widgets.TextInput(
            attrs={"class": "form-control"},
        ),
        error_messages={
            "invalid": "博客站点格式不正确！",
            "required": "博客站点不能为空哦",
        }
    )

    # blog_theme = forms.CharField(
    #     max_length=32,
    #     label="站点的css样式",
    #     widget=forms.widgets.TextInput(
    #         attrs={"class": "form-control"},
    #     ),
    #     error_messages={
    #         "invalid": "css格式不正确！",
    #         "required": "样式不能为空哦",
    #     }
    # )



    def clean_username(self):
        username = self.cleaned_data.get("username")
        is_exist = models.UserInfo.objects.filter(username=username)
        if is_exist:
            # 表示用户名已注册
            self.add_error("username",ValidationError("用户名已存在!"))
        else:
            return username
    def clean_email(self):
        email = self.cleaned_data.get("email")
        is_exist = models.UserInfo.objects.filter(email=email)
        if is_exist:
            # 表示用户名已注册
            self.add_error("email",ValidationError("邮箱已被注册!"))
        else:
            return email

    # 重写全局的钩子函数，对确认密码做校验
    def clean(self):
        password = self.cleaned_data.get("password")
        re_password = self.cleaned_data.get("re_password")

        if re_password and re_password != password:
            self.add_error("re_password", ValidationError("两次密码不一致"))

        else:
            return self.cleaned_data
