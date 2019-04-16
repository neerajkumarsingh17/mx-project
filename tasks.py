from __future__ import absolute_import

from enrollment.api import add_enrollment, get_enrollment
from celery.task import task
from django.contrib.auth.models import User
from celery.result import AsyncResult


@task
def enrollment_task(user, course):
    course_id = course
    users = user
    print(enrollment_task.request.id)
    #users_len -> count all users length 
    users_len = (User.objects.count())
    print('total users len count :--',users_len)
    if not users :
        i = 100
        count = 0
        cou = 0
        while True:
            users = User.objects.values_list('username', flat=True)[count:i]
            for user_name in users:
                try:
                    if not get_enrollment(user_name, course_id):
                        try:
                            add_enrollment(user_name, course_id, is_active=True)
                            cou  += 1
                        except:
                            pass
                        else:
                            print('user {0} is enroll in this course {1}'.format(user_name, course_id))
                    else:
                        cou  += 1
                        print('user {0} is already enroll in this course {1}'.format(user_name, course_id))
                        print(cou)
                        pass
                except Exception as e:
                    print(e)
            len_user = cou
            if (users_len == cou):
                break        
            count = i
            i += 100       
    else:                
        len_user = len(users) 
        i = 1
        count = 0
        cou = 0
        while True:
            selected_users = users[count:i]   
            for user_name in selected_users:
                try:
                    if not get_enrollment(user_name, course_id):
                        try:
                            add_enrollment(user_name, course_id, is_active=True)
                            cou  += 1
                        except:
                            pass
                        else:
                            print('user {0} is enroll in this course {1}'.format(user_name, course_id))
                    else:
                        print('user {0} is already enroll in this course {1}'.format(user_name, course_id))
                        cou  += 1
                        pass
                except Exception as e:
                    print(e)
            if (len_user == cou):
                break
            count = i
            i += 1
    return ("Enrollment complete")



    
