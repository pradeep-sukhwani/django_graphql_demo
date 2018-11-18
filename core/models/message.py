from django_extensions.db.models import TimeStampedModel, models


class Message(TimeStampedModel):
    user = models.ForeignKey('auth.User')
    message = models.TextField()
