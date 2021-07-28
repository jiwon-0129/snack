"""madcookie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
import eating.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new/', eating.views.new, name="new"),
    path('', eating.views.home, name="home"),
    path('review/<int:pk>', eating.views.review, name="review"),
    path("review/<int:review_id>", eating.views.detail, name="detail"),
    path('login/', eating.views.login_view, name="login"),
    path('logout/', eating.views.logout_view, name="logout"),
    path('register/', eating.views.register_view, name="signup"),
    path('create/', eating.views.create, name="create"),
    path('edit/<int:review_id>', eating.views.edit, name="edit"),
    path('update/<int:review_id>', eating.views.update, name="update"),
    path('delete/<int:review_id>', eating.views.delete, name="delete"),
    path('category/<int:category_id>', eating.views.category, name="category"),
    # path('signup/', eating.views.signup, name="signup"),
]
