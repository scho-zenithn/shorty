from django.shortcuts import render,redirect
from django.db.models import Q
from django.http import HttpResponse
from shorty.models import Surl

# Create your views here.


def index(request):
    return redirect('common:url')
    
    # # if request.method == "GET":
    # if request.user.is_authenticated:
    #     surls = Surl.objects.filter(owner__username=request.user.username)
    #     context = {'surls':surls}
    #     return render(request,'shorty/index.html',context=context)    

    # else:
    #     return render(request,'shorty/index.html')    

def surl(request,alias):
    domain=(request.get_host()).split(':')[0]

    try:
        surl = Surl.objects.filter(domain__name=domain).get(alias=alias)
        print(surl)
        
    except Surl.DoesNotExist:
        surl = False
    
    if surl:
        return redirect(surl.url)
    
    return HttpResponse(f"{domain}/{alias} is not exists")
