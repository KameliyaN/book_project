from django.shortcuts import render


# Create your views here
#
def index(request):
    return render(request,'books/index.html')


def create(request):
    pass


def edit(request):
    pass
