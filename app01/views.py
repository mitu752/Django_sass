from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from utils.email.mail import send_email


def send_email1(request):
    send_email("sakdfjfdj32423532959539952953@qq.com")
    return HttpResponse("success")


from django import forms
from app01 import models
from django.core.validators import RegexValidator


class RegisterModelForm(forms.ModelForm):
    mobile = forms.CharField(label="手机号", validators=[RegexValidator('/^1[3456789]\d{9}$/', '手机号格式错误')])
    password = forms.CharField(label="密码", widget=forms.PasswordInput())
    confirm_password = forms.CharField(label="重复密码", widget=forms.PasswordInput())
    code = forms.CharField(label="验证码")

    class Meta:
        model = models.UserInfo
        # fields = '__all__'
        fields = ('username', 'password', 'confirm_password', 'mobile', 'email', 'code')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 统一设置样式
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = '请输入{}'.format(field.label)


def register(request):
    form = RegisterModelForm()
    return render(request, 'register.html', {'form': form})
