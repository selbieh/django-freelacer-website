from django.shortcuts import render
from .forms import contact_us_form
from django.shortcuts import redirect,HttpResponseRedirect,reverse
def contact_us(request):
    if request.method=="POST":
        form=contact_us_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "contact_us/contact_us.html",locals())

    else:
        form=contact_us_form()
        return render(request,"contact_us/contact_us.html",{"form":form})

# Create your views here.
