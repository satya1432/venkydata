from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User

from ..mixins import TimeAuditModel

class DatabaseEngine(TimeAuditModel):

    name = models.CharField(max_length=255, unique=True)

    connection = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Database Engine"
        verbose_name_plural = "Database Engines"
        db_table = "database_engines"
    
    def __str__(self):
        return f"{self.name}"

class DatabaseConfig(TimeAuditModel):

    # database name
    name = models.CharField(max_length=255, unique=True)
    
    # database username
    user = models.CharField(max_length=255)
    
    # database password
    password = models.CharField(max_length=255)
    
    # database host
    host = models.CharField(max_length=255)
    
    # database port
    port = models.PositiveIntegerField()
    
    # database engine
    engine = models.ForeignKey(DatabaseEngine, on_delete=models.CASCADE)

    # user
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="databases")

    # database display name
    display_name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Database Config"
        verbose_name_plural = "Database Configs"
        db_table = "database_configs"
    
    def __str__(self):
        return f"{self.owner} - {self.name}"


class Query(TimeAuditModel):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)

    sql = models.TextField()

    description = models.TextField()

    engine = models.ForeignKey(DatabaseEngine, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Query"
        verbose_name_plural = "Queries"
        db_table = "queries"
    
    def __str__(self):
        return f"{self.user}"


