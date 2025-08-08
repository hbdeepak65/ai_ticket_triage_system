from django.db import models
from django.contrib.auth.models import User

# Optional User Profile extension (if needed later)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, default='Customer')  # or 'Agent', etc.

    def __str__(self):
        return self.user.username
