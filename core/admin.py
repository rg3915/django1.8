from django.contrib import admin
from .models import Distributor, Category, Movie


admin.site.register(Distributor)
admin.site.register(Category)
admin.site.register(Movie)
