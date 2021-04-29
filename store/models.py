from django.db import models

# Create your models here.
from django_logic import ProcessManager

from store.process import LockerProcess


class Lock(ProcessManager.bind_state_fields(status=LockerProcess), models.Model):
    status = models.CharField(
        choices=LockerProcess.states, default='open',
        max_length=16, blank=True)
    customer_received_notice = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.status
