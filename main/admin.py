from django.contrib import admin
from .models import User,Admin,Client,Storage

# Register your models here.
admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Client)
admin.site.register(Storage)
