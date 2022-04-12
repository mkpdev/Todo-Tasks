from django.db import models


class Task(models.Model):
    label = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.label


class SubTask(models.Model):
    task = models.ForeignKey(Task,
                             on_delete=models.CASCADE,
                             related_name="subtask",
                             blank=True,
                             null=True)
    label = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.label


class SubSubTask(models.Model):
    task = models.ForeignKey(SubTask,
                             on_delete=models.CASCADE,
                             related_name="subsubtask",
                             blank=True,
                             null=True)
    label = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.label
