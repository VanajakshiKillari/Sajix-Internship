from django.db import models
from django.core.exceptions import ValidationError

class Todo(models.Model):
    STATUS_CHOICES = [
        ('TODO', 'TODO'),
        ('IN_PROGRESS', 'IN-PROGRESS'),
        ('DONE', 'DONE'),
    ]

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)
    duration = models.IntegerField(default=6000, help_text="Duration in seconds. Minimum: 1, Maximum: 6000 (100 minutes)")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='TODO')

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if Todo.objects.filter(title=self.title).exists():
            raise ValidationError("A Todo with this name already exists.")
        super(Todo, self).save(*args, **kwargs)



    
