from django.contrib import admin
from ele.models import Menu_Item, Nazwa
class NazwaAdmin(admin.ModelAdmin):
	prepopulated_fields={'slug':('name',)}
admin.site.register(Menu_Item)
admin.site.register(Nazwa,NazwaAdmin)
# Register your models here.
