from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def post_details(request):
    return render(request, 'main/blog-single.html')