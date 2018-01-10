from django.http import HttpResqponse

def index(request):
    return HttpResponse('<h1>首页</h1>')
