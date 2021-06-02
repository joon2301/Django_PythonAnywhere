from django.contrib import admin
from .models import ForeignData, KoreanData
# Register your models here.
admin.site.register(ForeignData)
admin.site.register(KoreanData)