from os import sysconf
import os
from django.db import models
from django.contrib import admin
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from enmashcorp.settings import MEDIA_URL


class UploadedFile(models.Model):
    name = models.CharField(max_length=200)
    createdAt = models.DateTimeField(auto_created=True)
    file = models.FileField(upload_to='filestorage', max_length=500)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk is not None:
            originalFile = UploadedFile.objects.get(pk=self.pk)
            if originalFile.file != self.file:
                originalFile.file.delete(False)
        super(UploadedFile, self).save(*args, **kwargs)



@receiver(pre_delete, sender=UploadedFile)
def uploaded_file_pre_delete(sender, instance, **kwargs):
    instance.file.delete(False)


admin.site.register(UploadedFile)