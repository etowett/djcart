from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

from django.db import connection

from logging import getLogger
log = getLogger(__name__)


def home(request):
    return render(request, 'home.html')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


class HealthCheckView(View):
    """Health check endpoint to confirm if the site is up and db is reachable."""
    def get(self, request, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute("select 1")
            one = cursor.fetchone()[0]
        return JsonResponse({"success": True, "db": one})
