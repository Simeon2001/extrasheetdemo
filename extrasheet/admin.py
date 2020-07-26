from django.contrib import admin
from .models import User,Profile,Club,Club_in,Club_fo,Club_re,Notify
# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Club)
admin.site.register(Club_in)
admin.site.register(Club_fo)
admin.site.register(Club_re)
admin.site.register(Notify)

