from django.http import HttpResponse


def Home(request, name):
    return HttpResponse("Bonjour depuis Django  " + name)


def home(request):
    return HttpResponse("Bonjour depuis Django " )

