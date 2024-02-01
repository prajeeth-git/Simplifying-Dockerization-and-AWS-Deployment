from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.views import View

from analytics.models import ClickEvent

from .models import urlshortner,urlmanager
from .forms import submiturlform





class Homeview(View):
    def get(self,request,*args,**kwargs):
        the_form =submiturlform()
        context={
            "title":" URL",
            "form": the_form
        }
        return render(request,"shortener/home.html",context)

    def post(self,request,*args,**kwargs):

        form =submiturlform(request.POST)
        
        context={
            "title":" URL",
            "form": form
        }
        template = "shortener/home.html"
        if form.is_valid():
            print(form.cleaned_data)
            new_url=form.cleaned_data.get("url")
            # print(urlshortner,new_url,"aasafsw")
            obj,created = urlshortner.objects.get_or_create(url=new_url)
            context = {
                "object":obj,
                "created": created,
            }
            if created:
                template = "shortener/success.html"
            else:
                template = "shortener/already-exists.html"

        return render(request,template,context)


class urlview(View):

    def get(self,request,short=None,*args,**kwargs):
        qs = urlshortner.objects.filter(short__iexact=short)
        # obj=get_object_or_404(urlshortner,short=short)
        if qs.count() is 1 and not qs.exists():
            raise Http404
        obj = qs.first()
        print(ClickEvent.objects.create_event(obj))
        return HttpResponseRedirect(obj.url)
