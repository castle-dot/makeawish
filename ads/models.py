from django.db import models

# Create your models here.
from django.db import models

class AdBar(models.Model):
    title = models.CharField(max_length=100, blank=True, help_text="Optional title/alt text for the image")
    image = models.ImageField(upload_to='ad_bars/', help_text="Upload banner image (recommended size: 1200×300 or similar)")
    is_active = models.BooleanField(default=True, help_text="Only active ads show")
    display_order = models.PositiveIntegerField(default=0, help_text="Lower number = higher priority")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['display_order', '-created_at']
        verbose_name = "Ad Banner"
        verbose_name_plural = "Ad Banners"

    def __str__(self):
        return self.title or f"Ad Bar {self.id}"

    @classmethod
    def get_current(cls):
        """Get the first active ad (you can change logic later for rotation)"""
        return cls.objects.filter(is_active=True).first()