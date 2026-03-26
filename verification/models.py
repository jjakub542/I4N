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
    # Main content
    title = models.CharField(max_length=255)
    quote = models.TextField(help_text="The exact statement being verified.")
    text = models.TextField(help_text="Full explanation and verification details.")

    # Author info
    author_name = models.CharField(max_length=255)
    author_role = models.CharField(max_length=255, blank=True)

    # Metadata
    read_time_minutes = models.PositiveIntegerField(default=3)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    # Verification
    status = models.CharField(
        max_length=20,
        choices=VerificationStatus.choices,
        default=VerificationStatus.UNVERIFIED,
    )

    # Tags
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

    @property
    def author_initials(self):
        """Generate initials like JJ from 'Janusz Jędra'."""
        parts = self.author_name.split()
        return "".join(p[0].upper() for p in parts[:2])
