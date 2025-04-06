from django.contrib import admin

# Register your models here.
from .models import Flower
from .models import Track

admin.site.register(Flower)
admin.site.register(Track)