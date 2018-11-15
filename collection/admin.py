from django.contrib import admin
from collection.models import Meme
class MemeAdmin(admin.ModelAdmin):
    model = Meme
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Meme, MemeAdmin)
# Register your models here.
