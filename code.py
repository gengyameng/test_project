from django.http import HttpResqponse

def index(request):
    return HttpResponse('<h1>首页</h1>')

def index2(request):
    return HttpResponse('<h1>首页2</h1>')
