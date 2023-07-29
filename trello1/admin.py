from django.contrib import admin
from .models import *

admin.site.register(Organization)
admin.site.register(Location)
admin.site.register(Board)
admin.site.register(Member)
admin.site.register(Card)
admin.site.register(Checklist)

