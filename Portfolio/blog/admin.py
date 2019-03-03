from django.contrib import admin
from . import models

# Register your models here.这里和gallery比换了一种写法
admin.site.register(models.Blog)