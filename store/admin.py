from django.contrib import admin

from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Establishment)