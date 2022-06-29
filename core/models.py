from django.db import models

class Places(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name}'