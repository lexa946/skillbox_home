from django.contrib import admin
from django.http import HttpRequest
from django.db.models import QuerySet




@admin.action(description="Архивировать продукты")
def mark_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=True)

@admin.action(description="Разархивировать продукты")
def mark_unarchived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=False)


@admin.action(description="Нет в наличии")
def mark_no_has_now(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(has_now=False)

@admin.action(description="Есть в наличии")
def mark_has_now(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(has_now=True)