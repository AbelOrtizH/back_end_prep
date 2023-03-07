from django.contrib import admin
from .models import *

# Register your models here.
#admin.site.register(Logger)


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("name", "contact", "time", "count", "notes")
    search_fields = ("name", )