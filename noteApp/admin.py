from django.contrib import admin
from .models import Master, User, Note

# Register your models here.
admin.site.register(Master)
admin.site.register(User)
admin.site.register(Note)