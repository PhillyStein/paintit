from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
	is_artist = models.BooleanField(default=False)
	is_client = models.BooleanField(default=False)

class Client(AbstractUser):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	num_of_commissions = 0
	ratings = []
	reports = []


