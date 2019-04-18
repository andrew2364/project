from django.contrib import admin
from business.models import Arkans

class businessAdmin(admin.ModelAdmin):

    list_display = ['cel']


admin.site.register(Arkans, businessAdmin)