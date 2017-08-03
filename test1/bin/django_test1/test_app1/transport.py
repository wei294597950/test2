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






from django.contrib import admin
from test_app1.models import *
# Register your models here.
admin.site.register(deletelog)



class deletelog(models.Model):
    name=models.CharField(max_length=50)

    class Meta:
        verbose_name='删除日志'
        verbose_name_plural=verbose_name

    class Meta:
        permissions=(
            ("检索", "检索权限"),
            ("新增", "新增权限"),
            ("删除", "删除权限"),
            ("修改", "修改权限"),
            ("恢复", "恢复权限"),


        )


@login_required(login_url="/login/")

 if not request.user.has_perm('one.修改'):
    #@permission_required('one.修改')

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .forms import LoginForm

def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render_to_response('login.html', RequestContext(request, {'form': form,}))
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return render_to_response('list.html', RequestContext(request))
            else:
                return render_to_response('login.html', RequestContext(request, {'form': form,'password_is_wrong':True}))
        else:
            # return render_to_response('login.html', RequestContext(request, {'form': form,}))
            return render(request,'login.html',locals())

@login_required(login_url="/login/")
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login/")




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$',views.index,name='index'),
    url(r'^che/', views.che ,name="che"),
    # url(r'^test3/', views.test3 ,name="test3"),
    url(r'^listing/$', views.listing, name='listing'),
url(r'^form_edit/$', views.form_edit, name='form_edit'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
url(r'^logout/$',views.logout,name='logout'),
    url(r'^django_ajax/', views.django_ajax ,name="django_ajax")





         <div id="header-navbar-collapse" class="navbar-collapse collapse navbar-right">
                    <ul class="nav navbar-nav">

 <li>
                            <a href="#" >欢迎， <strong>{{ request.user.username }}</strong>
                            </a>
                       </li>
                        <li>
                            <a target="_parent" href="/logout/"><strong>注销</strong></a>
                        </li>
                    </ul>
	</div>