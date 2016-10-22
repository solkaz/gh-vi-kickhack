from django.http import HttpResponse
from django.views import generic


def index(request):
    return HttpResponse("Hello world!")


def GetNearbyShelters(request):
    if request.method == 'GET':
        print(request.GET)
    return HttpResponse("foo")


class IndexView(generic.TemplateView):
    template_name = 'gh_app/form.html'
