#from edxmako.shortcuts import render_to_response
from djangomako.shortcuts import render_to_response
from django.shortcuts import render
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from django.contrib.auth.models import User
from enrollment.api import add_enrollment, get_enrollment
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def course_date(request):
    course = CourseOverview.objects.only('id')
    users = User.objects.only('username')
    context = {
        'course': course,
        'users': users
    }
    return render(request, "mx-enrollment_new/mx-enrollment_new.html", context)
  

@api_view(['POST'])
def enroll_user(request):
    data= request.data
    data_dic=data.dict()
    course_id = data_dic['course']
    all_user_flag=data_dic['all_user']
    if all_user_flag == 'false':
      users = data_dic['users'].split(',')
    else:
      users = User.objects.only('username')
    sbar_max = len(users)
    count = 0 
    for user in users:
      try:
        if not get_enrollment(user, course_id):
          add_enrollment(user, course_id, is_active=True)
          count +=1
          print 'user {0} is enroll in this course {1}'.format(user, course_id)
          print 'User Number------------->', count
        else:
          print 'user {0} is already enroll in this course {1}'.format(user, count)
          count +=1
          print 'already enroll user count', count
          pass
      except Exception as e:
        print(e)

    return Response({"enrolled":'user enrolled', "count":count})












































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











