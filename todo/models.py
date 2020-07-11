from django.db import models

PRIORITY = (("danger","high"),("warning","normal"),("success","low"))
class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices = PRIORITY
    )
    duedate = models.DateField(null=True)
    # データのオブジェクトを文字列にする
    def __str__(self):
        return self.title

