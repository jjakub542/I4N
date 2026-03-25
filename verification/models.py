from django.db import models
from django.utils import timezone


class VerificationStatus(models.TextChoices):
    UNVERIFIED = "unverified", "Unverified"
    IN_PROGRESS = "in_progress", "In Progress"
    TRUE = "true", "True"
    FALSE = "false", "False"
    MISLEADING = "misleading", "Misleading"
    UNVERIFIABLE = "unverifiable", "Unverifiable"


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Statement(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    author = models.CharField(max_length=255, blank=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    status = models.CharField(
        max_length=20,
        choices=VerificationStatus.choices,
        default=VerificationStatus.UNVERIFIED,
    )

    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title
