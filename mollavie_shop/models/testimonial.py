from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    quote = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    is_visible = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} – {self.quote[:30]}..."
