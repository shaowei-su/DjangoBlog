import uuid
import datetime
import os

from django.shortcuts import render, render_to_response, redirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.models import User
from models import ActivateCode
from django.http import HttpResponse
from django.core.mail import send_mail


# Create your views here.

def register(request):
    error = ""
    if request.method == "GET":
        return render_to_response("usercenter_register.html",
                                  {},
                                  context_instance=RequestContext(request))
    else:
        username = request.POST["username"].strip()
        email = request.POST["email"].strip()
        password = request.POST["password"].strip()
        re_password = request.POST["re_password"].strip()
        if not username or not password or not email:
            error = "All fields need to be completed"
        if password != re_password:
            error = "Two passwords does not match"
        if User.objects.filter(username=username).count() > 0:
            error = "Already exist user"
        if not error:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.is_active = False
            user.save()

            new_code = str(uuid.uuid4()).replace("-", "")
            expire_time = datetime.datetime.now() + datetime.timedelta(days=2)
            code_record = ActivateCode(owner=user, code=new_code, expire_timestamp=expire_time)
            code_record.save()

            activate_link = "http://%s%s" % (request.get_host(), reverse("usercenter_activate", args=[new_code]))
            send_mail("The Django Forum Activation Email", "Your email address is %s" % activate_link, "iamajunkemailaddress@gmail.com",
                      [email], fail_silently=False)

        else:
            return render_to_response("usercenter_register.html",
                                      {"error" : error},
                                      context_instance=RequestContext(request))
        return redirect(reverse("login"))

def activate(request, code):
    query = ActivateCode.objects.filter(code=code, expire_timestamp__gte=datetime.datetime.now())
    if query.count() > 0:
        code_record = query[0]
        code_record.owner.is_active = True
        code_record.owner.save()
        return HttpResponse("Activation succeeded")
    else:
        return HttpResponse("Activation failed")