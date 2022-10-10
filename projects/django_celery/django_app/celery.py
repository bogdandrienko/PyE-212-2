import time

from celery import shared_task, current_task
from django.contrib.auth.models import User


# parsing(get data from another web-sites), analyze, reports, image refactor, send mass mail

@shared_task
def add(x, y):
    return x + y


@shared_task
def count_users():
    time.sleep(10.0)
    return User.objects.count()


@shared_task
def send_mass_email(recipients: list, message: dict, skip_error=True):
    time.sleep(20)
    return [(True, ""), (False, "timeout error")]
    results = []
    for recipient in recipients:
        success = False
        error = ""
        try:
            # send_mail(recipient, message)
            pass
        except Exception as error:
            print(error)
            error = error
            if skip_error is False:
                break
        else:
            success = True
        finally:
            results.append((success, error))
    # return results  # [(True, ""), (False, "timeout error")]
    return [(True, ""), (False, "timeout error")]


@shared_task
def send_email(self):
    # """Sends an email when the feedback form has been submitted."""
    #
    # sleep(20)  # Simulate expensive operation(s) that freeze Django
    #
    # send_mail(
    #
    #     "Your Feedback",
    #
    #     f"\t{self.cleaned_data['message']}\n\nThank you!",
    #
    #     "support@example.com",
    #
    #     [self.cleaned_data["email_address"]],
    #
    #     fail_silently=False,
    #
    # )
    pass
