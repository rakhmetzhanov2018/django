from django.http import HttpResponse
"""cfvbj;/'"""

def index(request):
    return HttpResponse("Hello, Welcome to list of questions. Select your topic: history (main_screen/historyQ/)")


def hq1(request):
    a = '''Question 1</br>
    В каком году была подписана Декларация независимости США?</br>
    1)1676</br>
    2)1678</br>
    3)1775</br>
    4)1776'''
    return HttpResponse(a)


def hq2(request):
    a = '''Каково было первоначальное название Нью-Йорка?</br>
1)Новый Амстердам</br>
2)Большое яблоко</br>
3)Имперский штат</br>
4)Готэм'''
    return HttpResponse(a)


def hq3(request):
    a = '''Как долго длилась Столетняя война?</br>
1)116 лет</br>
2)100 лет</br>
3)50 лет</br>
4)101 год'''
    return HttpResponse(a)


def his(request):
    return HttpResponse('To continue enter number of question (/hq1/, /hq2/, /hq3/)')


def geo(request):
    return HttpResponse('To continue enter number of question (/gq1/, /gq2/, /gq3/)')


def gq1(request):
    a = '''Высота горы Эверест составляет 29 029 футов. Но знаете ли вы, какая страна претендует на эту всемирно 
    известную достопримечательность?</br>
1)Колумбия</br>
2)Непал</br>
3)Швейцария</br>
4)Венесуэла'''
    return HttpResponse(a)


def gq2(request):
    a = '''Какая страна имеет аббревиатуру “CH”?</br>
1)Китай</br>
2)Швейцария</br>
3)Куба</br>
4)Чили'''


def gq3(request):
    a = '''Какой самый большой остров в мире?</br>
1)Исландия</br>
2)Финляндия</br>
3)Гренландия</br>
4)Ирландия'''


def empty(request):
    return HttpResponse('go to main_screen (/main_screen/)')
