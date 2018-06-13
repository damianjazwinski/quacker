from django.contrib import admin
from django.contrib.auth.models import Group
from application.models import *


class QuackAdmin(admin.ModelAdmin):
    list_display = ['quacker', 'content', 'created_at']
    list_filter = ['quacker', ]


admin.site.register(Quack, QuackAdmin)
admin.site.unregister(Group)