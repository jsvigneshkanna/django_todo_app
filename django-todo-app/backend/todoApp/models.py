from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=120)
    detail = models.TextField()
    isCompleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return "Title: " + self.title + " Detail: " + self.detail
