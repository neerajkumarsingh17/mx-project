from edxmako.shortcuts import render_to_response
from django.shortcuts import render
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from django.contrib.auth.models import User
from enrollment.api import add_enrollment
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect


def course_date(request):
  submitted = False
  if request.method=="POST":
    selected_option = request.POST.get('my_options', None)
    #selected_option_1 = request.POST.get('my_options_1', None)
    #if selected_option:
      #if selected_option.is_valid():
    return HttpResponseRedirect('/enrolled_data?submitted=True')
    
  else:
    course = CourseOverview.objects.only('id')
    users = User.objects.only('username')
    context = { 
        'course': course,
        'users': users
    }
  return render(request, "mx-enrollment_new/mx-enrollment_new.html", context)


""" 
@csrf_protect
def enrolled_data(request):
  if request.POST:  # If this is true, the view received POST
        selected_option = request.POST.get('my_options', None)
        if selected_option:
          enrolled_course = request.POST.get('enroll_course')  
        selected_option_user= request.POST.get('my_options_user', None)
        if selected_option:
          enrolled_user = request.POST.get('enrolled_user')
          
          add_enrollment(enrolled_user, enrolled_course)
          enrolled = {
            'enrolled_course': enrolled_course,
            'enrolled_user': enrolled_user
          }
  return render(request, "mx-enrollment_new/enrolled_data.html", {
      'enrolled_course': enrolled_course,
      'enrolled_user': enrolled_user
  })
 """


""" def course_date(request):
  submitted = False
  if request.method == "POST":
    selected_option = request.POST.get('my_options', None)
    if selected_option:
      if selected_option.is_valid():
        enrolled_course = request.POST.get('enroll_course')
        selected_option.save()
    selected_option_user = request.POST.get('my_options_user', None)
    if selected_option:
      if selected_option.is_valid():
        enrolled_user = request.POST.get('enrolled_user')
        selected_option.save()
        return HttpResponseRedirect('/enrolled_data?submitted=True') """











