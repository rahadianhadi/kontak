from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_response(request):
    return HttpResponse("<h1>Hello World</h1>")

def index(request):
    var_nama = "Rahadian"
    context = {
        "nama": var_nama,
    }

    return render(request, "majesti/index.html", context)