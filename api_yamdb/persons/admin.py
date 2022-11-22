from django.contrib import admin

from .models import Person


class PersonAdmin(admin.ModelAdmin):

    list_display = ('pk', 'name', 'id')
    search_fields = ('pk', 'name', 'id')
    list_filter = ('pk',)
    empty_value_display = '-пусто-'


admin.site.register(Person, PersonAdmin)
