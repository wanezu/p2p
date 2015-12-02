__author__ = 'root'
from django import forms
class ChangepwForm(forms.Form):
    '''
    修改密码表单
    '''
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={"required": "required","class":"txt","value":"","autocomplete":"off","id":"old_password",}),
                              max_length=20,error_messages={"required": "密码不能为空",})
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={"required": "required","class":"txt","value":"","autocomplete":"off","id":"new_password","data-stretype":"1",}),
                              max_length=20,error_messages={"required": "密码不能为空",})
    re_new_password = forms.CharField(widget=forms.PasswordInput(attrs={"required": "required","class":"txt","value":"","autocomplete":"off","id":"re_new_password",}),
                              max_length=20,error_messages={"required": "密码不能为空",})

class ChangephoneForm(forms.Form):
    '''
    修改手机号码
    '''
    code = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "验证码", "required": "required","id":"validNum","class":"txt w131 int_placeholder n-invalid","aria-required":"true","aria-invalid":"true","data-inputstatus":"error",}),
                              max_length=6,error_messages={"required": "验证码不能为空",})

class SearchForm(forms.Form):
    '''
    查询资金记录
    '''
    # log_info = forms.CharField(widget=forms.TextInput(attrs={"id":"log_info","name":"log_info","value":"","type":"hidden",}),required=False)
    start = forms.CharField(widget=forms.TextInput(attrs={"id":"dateInput1","class":"time_box","name":"start","value":"",}),required=False)
    end = forms.CharField(widget=forms.TextInput(attrs={"id":"dateInput2","class":"time_box j_date","name":"end","value":"",}),required=False)

class LoadForm(forms.Form):
    '''
    查询已投项目
    '''
    # status = forms.CharField(widget=forms.TextInput(attrs={"type":"hidden","name":"status","id":"status","value":"0",}),required=False)
    date_start = forms.CharField(widget=forms.TextInput(attrs={"id":"dateInput1","class":"time_box","name":"date_start","value":"",}),required=False)
    date_end = forms.CharField(widget=forms.TextInput(attrs={"id":"dateInput2","class":"time_box j_date","name":"date_end","value":"",}),required=False)