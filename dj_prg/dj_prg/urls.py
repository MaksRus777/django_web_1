"""
URL configuration for dj_prg project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from dj_app import views
urlpatterns = [
    #___статичные маршруты___


    path('admin/', admin.site.urls),
    path('',views.index, name = 'index'),
    path('about',views.about, name = 'about'),
    path('contact',views.contact, name = 'contact'),

    #___Динамические маршруты___
    path('product/<int:product_id>/<str:name>', views.product_1, name="product_1"),
    path('products', views.product_2, name='product_2'), #___передача данныъ по строке запроса способ 2


]
