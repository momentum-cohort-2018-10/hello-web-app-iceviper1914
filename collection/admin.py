from django.contrib import admin
from collection.models import Cheese
class CheeseAdmin(admin.ModelAdmin):
    model = Cheese
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Cheese, CheeseAdmin)
# Register your models here.
