from django.shortcuts import render
from verification.models import Statement

def home(request):
    statements = Statement.objects.order_by("-created_at")
    return render(request, "public/home.html", {
        "statements": statements
    })
