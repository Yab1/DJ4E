from django.contrib import admin
from .models import Cat, Dog, User

# Register your models here.
admin.site.register(User)
admin.site.register(Cat)
admin.site.register(Dog)
