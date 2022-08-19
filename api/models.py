from django.db import models

# Create your models here.
class Approval(models.Model):
    """Model definition for Approval."""
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

    def __str__(self):
        """Unicode representation of Approval."""
        return self.name
