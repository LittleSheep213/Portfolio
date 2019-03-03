from django.db import models

# Create your models here.


class Gallery(models.Model):
	title = models.CharField(default='作品名字', max_length=20)
	description = models.CharField(default='简单描述一下该作品', max_length=100)
	image = models.ImageField(default='default.png', upload_to='images/')

	def __str__(self):
		return self.title
