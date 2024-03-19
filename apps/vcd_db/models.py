from django.db import models


class Usermaster(models.Model):
    username = models.CharField(primary_key=True, max_length=6)
    userfullname = models.CharField(max_length=50)
    emailid = models.EmailField(max_length=50, blank=True, null=True)
    userpassword = models.CharField(max_length=100, blank=True, null=True)
    activeuser = models.CharField(max_length=1)
    createduser = models.CharField(max_length=6, blank=True, null=True)
    createddate = models.DateTimeField(blank=True, null=True)
    editeduser = models.CharField(max_length=6, blank=True, null=True)
    editeddate = models.DateTimeField(blank=True, null=True)

