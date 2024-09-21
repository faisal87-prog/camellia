from django.contrib import admin
from .models import Project, projectImage, Material, Door, doorColor, Location

admin.site.register(Project)
admin.site.register(projectImage)
admin.site.register(Material)
admin.site.register(Door)
admin.site.register(doorColor)
admin.site.register(Location)


