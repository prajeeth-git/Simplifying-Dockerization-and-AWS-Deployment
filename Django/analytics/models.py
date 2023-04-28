from django.db import models

# Create your models here.
from urlshortner.models import urlshortner

class ClickEventManager(models.Manager):
    def create_event(self,urlinstance):
        if isinstance(urlinstance,urlshortner):
            obj,created = self.get_or_create(view_url=urlinstance)
            obj.count+=1
            obj.save()
            return obj.count
        return None
class ClickEvent(models.Model):
    view_url=models.OneToOneField(urlshortner,any)
    count = models.IntegerField(default=0)
    time= models.DateTimeField(auto_now=True)
    timeupdate= models.DateTimeField(auto_now_add=True)

    objects=ClickEventManager()

    def __str__(self):
        return "{i}".format(i=self.count)