from django.shortcuts import render


def index(request):
    return render(request, "common/ciot.html")
