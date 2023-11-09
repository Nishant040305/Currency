from django.contrib import admin

# Register your models here.
from .models import History
from .models import favPain
admin.site.register(favPain)
admin.site.register(History)