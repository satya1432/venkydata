import json

from django.db import connection
from django.shortcuts import render
from django.http import JsonResponse
from django.db import connections
from django.conf import settings
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status

from ...db.models import DatabaseEngine, DatabaseConfig, Query
from ..serializers import (
    DatabaseEngineSerializer,
    DatabaseConfigSerializer,
    QuerySerializer,
)


def connect_database(db):
    db_config = {
        db.display_name: {
            "NAME": db.name,
            "USER": db.user,
            "PASSWORD": db.password,
            "HOST": db.host,
            "PORT": db.port,
            "ENGINE": db.engine.connection,
        }
    }
    return settings.DATABASES.update(db_config)


class DatabaseListCreate(views.APIView):
    def get(self, request):
        queryset = request.user.databases.all()
        serializer = DatabaseConfigSerializer(queryset, many=True)
        return render(request, "index.html", context={"data": serializer.data})

    def post(self, request):
        serializer = DatabaseConfigSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QueryGenerate(views.APIView):
    def post(self, request):
        db = request.data.get("db")
        db = request.user.databases.get(display_name=db)
        connect_database(db)
        conn = connections[db.display_name]
        cursor = conn.cursor()
        cursor.execute(request.data.get("query"))
        columns = [column[0] for column in cursor.description]
        print(columns)
        result = cursor.fetchall()
        return render(
            request, "result.html", context={"result": result, "columns": columns}
        )


def table_info(conn, cursor, table):
    model_data = {"model": table, "fields": []}
    fields = conn.introspection.get_table_description(cursor, table)
    for field in fields:
        model_data["fields"].append(
            {
                "name": field.name,
                "type": conn.introspection.get_field_type(field.type_code, field),
            }
        )
    return model_data


def get_schema(request, key):
    db = request.GET.get("db")
    db = request.user.databases.get(display_name=db)
    connect_database(db)
    conn = connections[db.display_name]
    cursor = conn.cursor()
    tables = conn.introspection.table_names(cursor)
    columns = []
    schema = []
    for table in tables:
        table_with_columns = table_info(conn, cursor, table)
        schema.append(table_with_columns)
        columns += table_with_columns["fields"]
    schema = {f"{conn.alias}": schema}
    data = {
        "columns": columns,
        "tables": tables,
        "schema": schema,
    }
    return data[key]


def get_tables(request):
    return JsonResponse(get_schema(request, "tables"), safe=False)


def get_columns(request):
    return JsonResponse(get_schema(request, "columns"), safe=False)


def show_schema(request):
    return render(
        request, "schema.html", context={"schema": get_schema(request, "schema")}
    )

