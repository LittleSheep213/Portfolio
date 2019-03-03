from django.shortcuts import render
from gallery.models import Gallery
# from blog.models import Blog


def home(request):
	gallerys = Gallery.objects
	# blogs = Blog.objects
	return render(request, 'home.html', {'gallerys': gallerys})