from django.db import models
from .util import code_generator,create_shortcode
from django.conf import settings
from .validators import validate_dot_com,validate_url

from django_hosts.resolvers import reverse
SHORT_MAX=getattr(settings,"SHORT_MAX",20)

class urlmanager(models.Manager):
    def all(self,*args,**kwargs):
        qs_main=super(urlmanager,self).all(*args,**kwargs)
        qs=qs_main.filter(active=True)
        return qs

    def refresh_codes(self,items=None):
        print(items)
        qs=urlshortner.objects.filter(id__gte=1)
        if items is not None and isinstance(items,int):
            qs = qs.order_by('-id')[:items]
        new_codes=0
        for q in qs:
            print(q)
            q.short=create_shortcode(q)
            print(q.short)
            q.save()
            new_codes+=1
        return "New codes made: {i}".format(i=new_codes)

# Create your models here.
class urlshortner(models.Model):
    url =models.CharField(max_length=220,validators=[validate_dot_com,validate_url])
    short =models.CharField(max_length=SHORT_MAX, unique=True,blank=True)
    time= models.DateTimeField(auto_now=True)
    timeupdate= models.DateTimeField(auto_now_add=True)
    active =models.BooleanField(default=True)

    objects=urlmanager()

    def save(self,*args,**kwargs):
        if self.short is None or self.short=="":
            print("saved")
            self.short=create_shortcode(self)
        if not "http" in self.url:
            self.url="http://" + self.url
        super(urlshortner,self).save(*args,**kwargs)


    def __str__(self):
        return str(self.url)

    def __str__(self):
        return str(self.url)

    def get_short_url(self):
        url_path=reverse("scode",kwargs={'short':self.short},host='www',scheme='http')
        return url_path
