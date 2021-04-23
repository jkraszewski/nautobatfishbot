# models.py
from django.db import models


class tests_to_run(models.Model):
    test_name = models.CharField(max_length=250)
    source_ip = models.CharField(max_length=250)
    source_port = models.CharField(max_length=250)
    dest_ip = models.CharField(max_length=250)
    dest_port = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class server_groups(models.Model):
    group_name = models.CharField(max_length=250)
    ip = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class port_groups(models.Model):
    group_name = models.CharField(max_length=250)
    port = models.CharField(max_length=250)

    def __str__(self):
        return self.name
