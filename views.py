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
# from django.template import RequestContext




# def course_date(request):
#   context = {'course':'',
#              'users':''
#              }
#   if request.method=="POST":
#     course_id = request.POST.get('course_id', None)
#     import pdb; pdb.set_trace()
#     if request.POST.get('user_id'):
#       usernames = request.POST.get('user_id').strip()
#     elif len(request.POST.get('numbers')):
#       usernames = request.POST.get('numbers').strip()
#     else:
#       usernames = 'ALL'
#     if not get_enrollment(usernames, course_id): 
#       if add_enrollment(usernames, course_id, is_active=True):
#         print 'successfull entrolled'
#     else:
#       print 'user {} is already entolled in course'.format(usernames)
#     return render(request, "mx-enrollment_new/mx-enrollment_new.html", context)

#   else:
#     course = CourseOverview.objects.only('id')
#     users = User.objects.only('username')
#     context = { 
#         'course': course,
#         'users': users
#     }
#   return render(request, "mx-enrollment_new/mx-enrollment_new.html", context)


  # if request.POST.get('user_id'):
  #           usernames = request.POST.get('user_id').strip()
  #       elif len(request.POST.get('numbers')):
  #           usernames = request.POST.get('numbers').strip()
  #       else:
  #           usernames = 'ALL'

    #user_id = request.POST.get('user_id', None)

@csrf_exempt
def course_date(request):
    course = CourseOverview.objects.only('id')
    users = User.objects.only('username')
    context = {
        'course': course,
        'users': users
    }
    return render(request, "mx-enrollment_new/mx-enrollment_new.html", context)
  
# def course_date(request):
#     course = CourseOverview.objects.only('id')
#     users = User.objects.only('username')
#     context = {
#         'course': course,
#         'users': users,
#         "csrftoken":csrf(request)['csrf_token']
#     }
#     return render_to_response("mx-enrollment_new/mx-enrollment_new.html", context)

@api_view(['POST'])
def enroll_user(request):
    import pdb; pdb.set_trace()
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
          pass
      except Exception as e:
        print(e)

    return Response({"enrolled":'user enrolled', "count":count})


# @api_view(['POST'])
# def enroll_user(request):
#     import json
#     import pdb; pdb.set_trace()
#     data_dic = request.data
#     # data_dic = json.load(data)
#     course_id = data_dic['course']
#     all_user_flag = data_dic['all_user']
#     if all_user_flag == 'false':
#       users = data_dic['users'].split(',')
#     else:
#       users = User.objects.only('username')
#     sbar_max = len(users)
#     count = 0
#     for user in users:
#       try:
#         if not get_enrollment(user, course_id):
#           add_enrollment(user, course_id, is_active=True)
#           count += 1
#           print 'user {0} is enroll in this course {1}'.format(user, course_id)
#           print 'User Number------------->', count
#         else:
#           print 'user {0} is already enroll in this course {1}'.format(user, count)
#           count
#           pass
#       except Exception as e:
#         print(e)

#     return Response({"enrolled": 'user enrolled', "count": count})













































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











