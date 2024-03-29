from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    image = models.ImageField(upload_to='users_img', null=True, blank=True)
    bio = models.CharField(max_length=400)
    PENDING = 'pending'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'

    FRIENDSHIP_STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected'),
    ]

    friends = models.ManyToManyField("self", through='Friendship', symmetrical=True)

    def __str__(self):
        return self.username
class Friendship(models.Model):
    from_user = models.ForeignKey(User, related_name='friendship_from', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='friendship_to', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=User.FRIENDSHIP_STATUS_CHOICES, default=User.PENDING)

    def __str__(self):
        return f"{self.from_user} <-> {self.to_user} ({self.status})"
# Create your models here.
