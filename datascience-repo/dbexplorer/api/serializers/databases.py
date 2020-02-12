from rest_framework import serializers
from ...db.models import DatabaseConfig, DatabaseEngine, Query


class DatabaseConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatabaseConfig
        fields = ("name", "host", "user", "password", "port", "engine", "owner", "display_name")

class DatabaseEngineSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatabaseEngine
        fields = ("name", "connection")

class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = "__all__"