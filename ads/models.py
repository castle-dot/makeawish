from django.db import models


class AdBar(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image_url = models.URLField(max_length=500, blank=True, null=True)
    video_url = models.URLField(max_length=500, blank=True, null=True, help_text="Direct video URL (MP4, auto-plays muted)")
    is_active = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    # ... classmethod get_current() if you have it ...