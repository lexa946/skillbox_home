from datetime import datetime, timedelta
from http import HTTPStatus

from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


class ThrottlingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.bucket: dict[str, datetime] = {}
        self.rate_ms = settings.THROTTLING_RATE_MS

    @classmethod
    def get_client_ip(cls, request: HttpRequest):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip

    def request_is_allowed(self, client_ip: str) -> bool:
        now = datetime.utcnow()
        last_access = self.bucket.get(client_ip)
        if not last_access:
            return True
        if (now - last_access) > timedelta(milliseconds=self.rate_ms):
            return True
        return False

    def __call__(self, request: HttpRequest):
        client_ip = self.get_client_ip(request)
        if self.request_is_allowed(client_ip):
            response = self.get_response(request)
            self.bucket[client_ip] = datetime.utcnow()
        else:
            response = HttpResponse("Rate linmit exceeded", status=HTTPStatus.TOO_MANY_REQUESTS)
        return response
