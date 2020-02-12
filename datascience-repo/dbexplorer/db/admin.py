from django.contrib import admin
from .models import DatabaseConfig, DatabaseEngine, Query

# Register your models here.
admin.site.register(DatabaseEngine)
admin.site.register(DatabaseConfig)
admin.site.register(Query)
