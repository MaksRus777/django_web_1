from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

#

# главная
def index(request):
    return HttpResponse("<h2>Привет</h2>")  # Способ 1 записать внутрь HTML код
    pass
# о себе
def about(request):
    return HttpResponseRedirect("/")  # редирект на главную страницу

def contact(request): # 3 способ с использованием HTML аблона
    name ='Вася'
    number = '37529999999'
    context = {'NUMBER': number, 'NAME': name}# Способ для передачи данных из питон в HTMl
    return render(request, "contact.html", context=context)


