from django.db import models
from django.conf import settings


# to give location in the model below
def upload_status_image(instance, filename):
    return 'local/{user}/{filename}'.format(user=instance, filename=filename)


# both of these classes are bult in and used to filter data when retrieving
class StatusQueryset(models.QuerySet):
    pass


class StatusManager(models.Manager):
    def get_queryser(self):
        return StatusQueryset(self.model, using=self._db)


class Status(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_status_image, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)[:50]

    class Meta:
        verbose_name = 'Status post'
        verbose_name_plural = 'Status posts'

    @property
    def owner(self):
        return self.user
