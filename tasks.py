from __future__ import absolute_import

from enrollment.api import add_enrollment, get_enrollment
from celery.task import task
from celery import current_task
from celery.result import AsyncResult


@task
def enrollment_task(user, course):
    user_id = user
    course_id = course
    count = 0
    for user_name in user_id:
        try:
            if not get_enrollment(user_name, course_id):
                try:
                    add_enrollment(user_name, course_id, is_active=True)
                except:
                    pass
                else:
                    count += 1
                    print('user {0} is enroll in this course {1}'.format(user_name, course_id))
                    print('User Number------------->', count)
            else:
                print('user {0} is already enroll in this course {1}'.format(user_name, count))
            pass
        except Exception as e:
            print(e)
    return ("Enrollment complete")