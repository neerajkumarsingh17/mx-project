import json
from djangomako.shortcuts import render_to_response
from django.shortcuts import render
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from django.contrib.auth.models import User
from enrollment.api import add_enrollment, get_enrollment
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from celery import uuid
from celery.result import AsyncResult
from django.http import HttpResponse
from .tasks import enrollment_task


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
    data = request.data
    data_dic = data.dict()
    course_id = data_dic['course']
    all_user_flag = data_dic['all_user']
    if all_user_flag == 'false':
        users = data_dic['users'].split(',')
    else:
        users = list()
        for user in User.objects.all():
            users.append(user.username)
    #length of the user
    sbar_max = len(users)
    #call task function
    enroll_task = enrollment_task.delay(users, course_id)
    #create task id
    task_id = uuid()
    print(enroll_task.task_id)
    print(enroll_task.status)

    enroll_task_status = enroll_task.status
    enroll_task_task_id = enroll_task.task_id
    res_data = {
        'enroll_task_status': str(enroll_task_status),
        'enroll_task_task_id': enroll_task_task_id
    }

    return Response(res_data)


@csrf_exempt
@api_view(['POST'])
def check_status(request):
    rec_data = request.data
    rec_data_dic = rec_data.dict()
    task_id = rec_data_dic['current_result']
    result_status = AsyncResult(task_id)
    data_1 = result_status.result or result_status.state
    task_status = {
        'data_1': data_1
    }
    return Response(task_status)


# def get_progress(request, task_id):
#     result = AsyncResult(task_id)
#     response_data = {
#         'state': result.state,
#         'details': result.info,
#     }
#     return HttpResponse(json.dumps(response_data), content_type='application/json')
