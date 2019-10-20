from django.shortcuts import render ,HttpResponse
from .forms import advir_form
from django.contrib.auth.decorators import login_required
from .models import adver_m
from  datetime import date
from django.core.paginator import  Paginator
from  django.shortcuts import redirect
@login_required(login_url="/accounts/login/")
def add_adv(request):
    if request.method=='POST':
        form=advir_form(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user=request.user
            instance.save()
            return redirect("/advertis/my_advertises/")
        else:
            return render(request, 'Advertis/adver.html', locals())

    else:
        form=advir_form()
        con={"form":form}
        return render(request,'Advertis/adver.html',con)

def view_adv(request):
    all_adv_list=adver_m.objects.all().filter(status="approved").order_by("-date")
    paginator = Paginator(all_adv_list, 10)
    page = request.GET.get('page')
    all_adv = paginator.get_page(page)
    return render(request,"Advertis/view-adv.html",context={"all_adv":all_adv})

@login_required(login_url="/login/")
def adv_details(request,adv_id):
     adv=adver_m.objects.get(pk=adv_id)
     creation_date=adv.date
     since=date.today()-creation_date
     return render(request,"Advertis/adv_details.html",context={"adv":adv , "since":since})


def my_advertises(request):
    request_user=request.user
    all_user_adv=adver_m.objects.all().filter(user=request_user).order_by("-date")
    paginator = Paginator(all_user_adv, 10)
    page = request.GET.get('page')
    user_adv = paginator.get_page(page)

    return render(request,"Advertis/my_adverises.html",context={"user_adv":user_adv})


def edit_adv(request,adv_id):
    req_user=request.user
    query=adver_m.objects.get(pk=adv_id)
    creat_user=query.user
    if req_user==creat_user:
        if request.method=="POST":
            form=advir_form(request.POST,instance=query)
            if form.is_valid:
                form.save()
                return redirect("/advertis/my_advertises")
        else:
            form=advir_form(instance=query)
            return render(request,"Advertis/edit-adv.html",{"form":form})
        adver_m.delete(pk=adv_id)
    else:
        return HttpResponse("you are not authurided to edit this post")



def delete_adv(request,adv_id):
    adver_m.objects.filter(pk=adv_id).delete()
    return redirect("/advertis/my_advertises")