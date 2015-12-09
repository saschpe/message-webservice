from django.db import models


class Message(models.Model):
    '''Message to user.
    '''
    MESSAGE_INFO = 'info'
    MESSAGE_UPDATE = 'update'
    MESSAGE_KILL = 'kill'
    MESSAGE_CHOICES = (
        (MESSAGE_INFO, 'Information'),
        (MESSAGE_UPDATE, 'Update notice'),
        (MESSAGE_KILL, 'App disabled'),
    )

    title = models.CharField(max_length=200)
    body = models.TextField()
    type = models.CharField(max_length=10, choices=MESSAGE_CHOICES, default=MESSAGE_INFO)

    class Meta:
        ordering = ['type', 'title']

    def __str__(self):
        return self.title


class ProductPlatform(models.Model):
    '''Product platforms.
    '''
    title = models.CharField(max_length=64, help_text='Platform name, e.g. "iOS"')

    def __str__(self):
        return self.title


class ProductFlavor(models.Model):
    '''Product flavor.
    '''
    title = models.CharField(max_length=64, help_text='Flavor name, e.g. "universal"')
    platform = models.ForeignKey(ProductPlatform)

    def __str__(self):
        return self.title


class Version(models.Model):
    '''Version.

    Maps specific messages to product platforms / flavors.
    '''
    version = models.CharField(max_length=32, help_text='Version string, e.g. "1.2.3"')
    flavor = models.ForeignKey(ProductFlavor, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200, blank=True, help_text='Add any information here (not returned by API)')

    def __str__(self):
        return self.version
