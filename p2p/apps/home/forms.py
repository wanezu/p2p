__author__ = 'root'
from django import forms
class RegForm(forms.Form):
    '''
    注册表单
    '''
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "用户名", "required": "required",}),
                              max_length=50,error_messages={"required": "用户名不能为空",})
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "邮箱", "required": "required",}),
                              max_length=50,error_messages={"required": "邮箱不能为空",})
    url = forms.URLField(widget=forms.TextInput(attrs={"placeholder": "Url", }),
                              max_length=100, required=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "密码", "required": "required",}),
                              max_length=20,error_messages={"required": "密码不能为空",})

class LoginForm(forms.Form):
    '''
    登录Form
    '''
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "用户名", "required": "required",}),
                              max_length=50,error_messages={"required": "用户名不能为空",})
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "密码", "required": "required",}),
                              max_length=20,error_messages={"required": "密码不能为空",})