from django.contrib import admin
from .models import Eating, HashTag, Review, Category

# Register your models here.
admin.site.register(Review)
admin.site.register(HashTag)
admin.site.register(Eating)
admin.site.register(Category)