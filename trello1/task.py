from celery import shared_task
from django.contrib.auth.models import User
from django.core.mail import send_mail

from Trello import settings
from trello1.models import Profile


@shared_task()
def send_email(subject,message,from_email,recipient_list):
    # Code to send the email asynchronously
    #
    # subject = "Trello Card Reminder"
    # message = "This is an async email sent using Celery vanshi ❤, to let you know your card is still in ToDo or Doing."
    # from_email = settings.EMAIL_HOST_USER
    # recipient_list = []
    # users = User.objects.filter(user_type='organization_admin')
    # for user in users:
    #     profile = Profile.objects.select_related("user", "organization").get(user=user)
    #     organization = profile.organization
    #     boards = organization.boards.prefetch_related("cards_on_board__user__user")
    #
    #     for board in boards:
    #         cards = board.cards_on_board.all()
    #         for card in cards:
    #             recipient_list.append(card.user.user.email)

    send_mail(subject, message, from_email, recipient_list)
    print("start")
