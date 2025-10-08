from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime
# Create your views here.

#

# главная
def index(request):
    html = ''
    menu1 ="<a href='/about'>о себе</a>"
    menu2 ="<a href='/contact'>контакты</a>"
    btn1 = "<a href ='/product/10/Nokia'> Продукты (способ 1)</a>"
    btn2 = "<a href ='/products?product_id=8&name=Samsung'> Продукты (способ 2)</a>"
    btn3 = "<a href ='/product/6?name=LG'> Продукты (способ 3)</a>"
    html = "<h2>{}</h2><br> {} {}<br>{}<br>{}<br>{}".format("Главная страница", menu1,menu2,btn1,btn2,btn3)

    return HttpResponse(html)  # Способ 1 записать внутрь HTML код
    pass
# о себе
def about(request):
    return HttpResponseRedirect("/")  # редирект на главную страницу

def contact(request): # 3 способ с использованием HTML аблона

    name ='Вася'
    time = datetime.now()
    number = '37529999999'
    names = ["Осипов Егор", "Воробьева Рената"]
    context = {'NUMBER': number, 'NAME': name, "TIME":time,"NAMES": names}# Способ для передачи данных из питон в HTMl

    return render(request, "contact.html", context=context)

def products(request):
    product_id =request.GET.get("product_id")
    return HttpResponse("Продукт №{}".format(product_id))
