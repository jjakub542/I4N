from django.db import models

class HomePage(models.Model):
    title = models.CharField(max_length=200, default="Nuclear Fact Checker")
    subtitle = models.CharField(max_length=300, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Homepage Content"
        verbose_name_plural = "Homepage Content"

    def __str__(self):
        return self.title

