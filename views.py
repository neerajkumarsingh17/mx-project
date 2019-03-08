from edxmako.shortcuts import render_to_response
from rest_framework.decorators import api_view
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from django.contrib.auth.models import User


def course_date(request):
  course = CourseOverview.objects.only('id')
  users = User.objects.only('username')
    
  context = {
    'course': course,
    'users': users
  }
  return render_to_response("mx-enrollment_new/mx-enrollment_new.html", context)


def add_enrollment(user_id, course_id, mode=None, is_active=True):
    """Enrolls a user in a course.

    Enrolls a user in a course. If the mode is not specified, this will default to `CourseMode.DEFAULT_MODE_SLUG`.

    Arguments:
        user_id (str): The user to enroll.
        course_id (str): The course to enroll the user in.

    Keyword Arguments:
        mode (str): Optional argument for the type of enrollment to create. Ex. 'audit', 'honor', 'verified',
            'professional'. If not specified, this defaults to the default course mode.
        is_active (boolean): Optional argument for making the new enrollment inactive. If not specified, is_active
            defaults to True.

    Returns:
        A serializable dictionary of the new course enrollment.

    Example:
        >>> add_enrollment("Bob", "edX/DemoX/2014T2", mode="audit")
        {
            "created": "2014-10-20T20:18:00Z",
            "mode": "audit",
            "is_active": True,
            "user": "Bob",
            "course": {
                "course_id": "edX/DemoX/2014T2",
                "enrollment_end": "2014-12-20T20:18:00Z",
                "enrollment_start": "2014-10-15T20:18:00Z",
                "course_start": "2015-02-03T00:00:00Z",
                "course_end": "2015-05-06T00:00:00Z",
                "course_modes": [
                    {
                        "slug": "audit",
                        "name": "Audit",
                        "min_price": 0,
                        "suggested_prices": "",
                        "currency": "usd",
                        "expiration_datetime": null,
                        "description": null,
                        "sku": null,
                        "bulk_sku": null
                    }
                ],
                "invite_only": False
            }
        }
    """
    if mode is None:
        mode = _default_course_mode(course_id)
    _validate_course_mode(course_id, mode, is_active=is_active)
    return _data_api().create_course_enrollment(user_id, course_id, mode, is_active)











