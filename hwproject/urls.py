"""hwproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import hw.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hw.views.firstPage, name='firstpage'),
    path('ppt/<student_name>', hw.views.ppt, name='ppt'),
    path('report/<student_name>', hw.views.report, name='report'),
    path('login/',hw.views.login, name='login'),
    path('signup/',hw.views.signup, name='signup'),
    path('logout/',hw.views.logout, name='logout'),
    path('home/<student_name>',hw.views.home, name='home'),
    path('qna/<student_name>/create',hw.views.create, name='create'),
    path('qna/<student_name>/detail/<blog_id>', hw.views.detail , name='detail'),
    path('qna/<student_name>', hw.views.qna, name='qna'),
    path('qna/<student_name>/new', hw.views.new, name="new"),
    path('qna/<student_name>/edit/<blog_id>', hw.views.edit, name="edit"),
    path('qna/<student_name>/update/<blog_id>', hw.views.update, name="update"),
    path('qna/<student_name>/delete/<blog_id>', hw.views.delete, name="delete"),
]
