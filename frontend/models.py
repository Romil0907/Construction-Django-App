from django.db import models

# Create your models here.


class post(models.Model):
    post_id = models.IntegerField()
    postname = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.post_id}: {self.postname}"


class cvModel(models.Model):
    # name = models.CharField(max_length=200)
    cv = models.FileField()
    post = models.ForeignKey(post, blank=True, on_delete=models.CASCADE)

    # def __str__(self):
    #      return self.name