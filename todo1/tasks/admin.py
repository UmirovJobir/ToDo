from django.contrib import admin
from .models import Task, Image, Title


# Register your models here.

admin.site.register(Task)
admin.site.register(Image)
admin.site.register(Title)


admin.site.site_header = 'Geeks For Geeks'
admin.site.site_title = 'GFG'
admin.site.index_title = 'Welcome Geeks'