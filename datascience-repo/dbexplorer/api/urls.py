from django.urls import path
from .views import (
    DatabaseListCreate,
    show_schema,
    QueryGenerate,
    get_tables,
    get_columns,
)

# Create your urls here.

urlpatterns = [
    path("db/", DatabaseListCreate.as_view(), name="list_databases"),
    path("schema/", show_schema, name="show_schema"),
    path("tables/", get_tables, name="get_tables"),
    path("columns/", get_columns, name="get_columns"),
    path("query/", QueryGenerate.as_view(), name="new_query"),
]
