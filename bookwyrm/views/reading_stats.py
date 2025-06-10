"""all years read books stats"""
from datetime import date
from uuid import uuid4

from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Sum, Min, Case, When
from django.http import Http404
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.views import View
from django.views.decorators.http import require_POST

from bookwyrm import models
from .helpers import get_user_from_username


# December day of first availability
FIRST_DAY = 15
# January day of last availability, 0 for no availability in Jan.
LAST_DAY = 15


# pylint: disable= no-self-use
class ReadingStats(View):
    """display an overview of all years"""

    def get(self, request, username): 
        """get response"""

        user = get_user_from_username(request.user, username)

        # TODO: make sure the info is sorted by year (decreasing) before sending it
        data = { 
            "stats_by_year" : [{"year": 2025, "books": 2, "pages": 200}, {"year": 2024, "books": 5, "pages": 500}, {"year": 2023, "books": 10, "pages": 1000}],
        }
        # TODO: check if the percentage will be computed here on in the frontend
        data = { 
            "stats_by_year" : [{"year": 2025, "books": 20, "pages": 20}, {"year": 2024, "books": 50, "pages": 50}, {"year": 2023, "books": 30, "pages": 30}],
        }

        return TemplateResponse(request, "user/reading_stats.html", data)


