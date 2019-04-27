from django.contrib import admin
from business.models import Arkans

class businessAdmin(admin.ModelAdmin):

    list_display = ['arkan_number','cel','osnova','jertva']


admin.site.register(Arkans, businessAdmin)