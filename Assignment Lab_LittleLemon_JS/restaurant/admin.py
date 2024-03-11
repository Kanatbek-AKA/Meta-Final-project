from django.contrib import admin

# Register your models here.
from .models import Menu, Booking, Book, MenuItem


admin.site.register(Menu)
admin.site.register(Booking)
#
admin.site.register(MenuItem)
admin.site.register(Book)
