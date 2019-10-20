from django.urls import path,include
from django.conf.urls import url
from . import views


urlpatterns = [
    #accout manage path
    path('', include('registration.backends.default.urls')),
    # profile
    url(r'^edit-profile/$',views.edit_profile,name="edit_profile"),
    url(r'^profile/$',views.profile,name="profile"),
    #home page
    url(r'^about_us/$',views.about_us,name="about_us"),
    url(r'^licence/$', views.licence, name="licence"),

    #main account data
    url(r'^personal/$',views.personal,name="personal"),
    url(r'^view_account_details/$', views.view_account_details, name="view_account_details"),

    url(r'^password/$',views.password_change,name='password_change'),
    url(r"^find-employee/$",views.find_employee,name="find_employee"),
    url(r'^find-employee/(?P<usr_id>[0-9]*)$',views.view_emp_profile,name="view_emp_profile")
]




