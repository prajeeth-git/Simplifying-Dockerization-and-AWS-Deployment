import random
import string
from django.conf import settings

SHORT_MIN=getattr(settings,"SHORT_MIN",10)

def code_generator(size=SHORT_MIN,chars=string.ascii_lowercase+string.digits):
    new_url=""
    for _ in range(size):
        new_url += random.choice(chars)
    return new_url

def create_shortcode(instance,size=SHORT_MIN):
    new_code=code_generator(size=size)
    url_class=instance.__class__
    # print(url_class)
    # print(instance,'dds')
    # print(instance.__class__.__name__)
    check=url_class.objects.filter(short=new_code).exists()
    if check:
        return create_shortcode(size=size)
    return new_code