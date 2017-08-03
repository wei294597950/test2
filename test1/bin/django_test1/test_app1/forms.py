#coding:utf-8

from django import forms
from django.contrib.auth.models import User
class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label="用户名",
        error_messages={'required': '请输入用户名'},
        widget=forms.TextInput(
            attrs={
                'placeholder':"用户名",
            }
        ),
    )
    password = forms.CharField(
        required=True,
        label="密码",
        error_messages={'required': '请输入密码'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder': "密码",
            }
        ),
    )
    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError("用户名和密码为必填项")
        else:
            cleaned_data = super(LoginForm, self).clean()



clusters = (
          ('es_offline', 'es_offline'),
            ('es_online', 'es_online'),
            )
indexs=(
                ("chat_test","chat_test"),
                        ("chat_test2","chat_test2"),
                        )
class searchform(forms.Form):
    #cluster = forms.ChoiceField(choices=clusters,label="cluster", error_messages={"required": "这个项必须填写"})
    #index = forms.ChoiceField(choices=indexs,label="index", error_messages={"required": "这个项必须填写"})
    #types=forms.CharField(label="type",error_messages={"required":"这个项必须填写"})
    query=forms.CharField(label="query",error_messages={"required":"这个项必须填写"})
    answer=forms.CharField(label="answer",required=False)
    


class editform(forms.Form):
    clusters = forms.ChoiceField(choices=clusters,label="clusters")
    indexs=forms.CharField(label="index")
    typess=forms.CharField(label="types")
    qaid=forms.CharField(label="id")
    newanswer=forms.CharField(label="new answer")



    
class addform(forms.Form):
    cluster = forms.ChoiceField(choices=clusters,label="cluster", error_messages={"required": "这个项必须填写"})
    index = forms.ChoiceField(choices=indexs,label="index", error_messages={"required": "这个项必须填写"})
    types=forms.CharField(label="type",error_messages={"required":"这个项必须填写"})
    query=forms.CharField(label="query",error_messages={"required":"这个项必须填写"})
    answer=forms.CharField(label="answer",error_messages={"required":"这个项必须填写"})





