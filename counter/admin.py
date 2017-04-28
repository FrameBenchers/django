from django.contrib import admin
from counter.models import Counter

class CounterAdmin(admin.ModelAdmin):
    list_display = ('pk', 'value')

admin.site.register(Counter, CounterAdmin)
