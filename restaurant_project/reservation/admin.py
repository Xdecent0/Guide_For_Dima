from django.contrib import admin
from .models import UserProfile, Table, Reservation

admin.site.register(UserProfile)
admin.site.register(Table)
admin.site.register(Reservation)