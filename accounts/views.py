from django.shortcuts import render ,reverse,HttpResponseRedirect
from . forms import profile_form,personal_f
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required




def edit_profile(request):
    if request.method=="POST":
        form=profile_form(request.POST or None, request.FILES or None ,instance=request.user.profile)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(reverse("profile"))
        else:
            return render(request, "edit-profile.html", locals())

    else:
        form=profile_form(instance=request.user.profile)
        return render(request,"edit-profile.html",{"form":form})





def profile(request):
    user=request.user
    return render(request,'profile.html',{'user':user})


def personal(request):
    if request.method=="POST":
        form=personal_f(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "personal.html", locals())


    else:
        form=personal_f(instance=request.user)
        arg={"form":form}
        return render(request,"personal.html",arg)

def view_account_details(request):
    user=request.user
    return render(request,"view_account_details.html",{"user":user})


def password_change(request):
    return HttpResponseRedirect(reverse("auth_password_change"))






def find_employee(request):
    query_set_list=User.objects.all().filter(profile__free_lancer=True).order_by("-date_joined")
    paginator=Paginator(query_set_list,9)
    page = request.GET.get('page')
    query_set = paginator.get_page(page)
    return render(request,"find-employee.html",context={"query_set":query_set})






@login_required(login_url="/login")
def view_emp_profile(request,usr_id):
    user=User.objects.get(pk=usr_id)
    return render(request,"employee_profile.html",context={"user":user})




def about_us(request):
    return render(request,"about us.html")

def licence(request):
    return render(request,"licence.html")

