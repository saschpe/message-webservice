from django.db import models


class Message(models.Model):
    '''Message to user.
    '''
    MESSAGE_INFO = 'info'
    MESSAGE_UPDATE = 'update'
    MESSAGE_KILL = 'kill'
    MESSAGE_CHOICES =(
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


class Version(models.Model):
    '''Application version

    Points to exactly one message.
    '''
    version = models.CharField(max_length=200, help_text="Version string, e.g. 1.2.3")
    messages = models.ForeignKey(Message, on_delete=models.CASCADE)

    def __str__(self):
        return self.version
