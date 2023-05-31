from django.contrib import admin
from .models import Flight,Airport,Pasenger

class FlightrAdmin(admin.ModelAdmin):
    list_display=('id','origin','destination','duration')

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ('flights',)

admin.site.register(Airport)
admin.site.register(Flight, FlightrAdmin)
admin.site.register(Pasenger, PassengerAdmin)
# Register your models here.
