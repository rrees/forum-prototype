import uuid

from django.db import models

# Create your models here.

FORUM_TITLE_MAX = 300
FORUM_POST_SUBJECT_MAX = 255


class Forum(models.Model):
    title = models.CharField(max_length=FORUM_TITLE_MAX)
    external_id = models.UUIDField(default=uuid.uuid4, editable=False)


class Post(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    external_id = models.UUIDField(default=uuid.uuid4, editable=False)
    subject = models.CharField(max_length=FORUM_POST_SUBJECT_MAX, null=True)
    content = models.TextField()
