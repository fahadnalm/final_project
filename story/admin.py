from django.contrib import admin
from .models import Story, Page, Option


class OptionInline(admin.StackedInline):
    model = Option
    fk_name = 'page'


class PageAdmin(admin.ModelAdmin):
    inlines = [OptionInline]

admin.site.register(Story)
admin.site.register(Page, PageAdmin)
admin.site.register(Option)
