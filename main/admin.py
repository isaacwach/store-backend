from django.contrib import admin
from .models import User,Admin,Client,Storage

from .models import Booking,Transport

# Register your models here.

admin.site.register(Booking)
admin.site.register(Transport)

admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Client)
admin.site.register(Storage)

