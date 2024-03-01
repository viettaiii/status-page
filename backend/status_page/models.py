from django.db import models


class Component(models.Model):
    title = models.CharField(max_length=200)
    OPERATIONAL = 'Operational'
    MAINTENANCE = 'Maintenance'

    CHOICES = (
        (OPERATIONAL, OPERATIONAL),
        (MAINTENANCE, MAINTENANCE),
    )
    status = models.TextField(choices=CHOICES, default=OPERATIONAL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
