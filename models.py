from django.dp import models
from django.core.validators import Minlengthvalidator

class pokemon(models.Model):
    health = models.intergerfield(validators={MinlengthValidators})