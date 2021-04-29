

def turn_on_alarm(*args, **kwargs):
    # from .models import Lock
    # lock = Lock.objects.get(id=1)
    # print("lock ", lock)
    # lock.customer_received_notice = True
    # lock.save()
    print("****** Trigger any process **", args)
    print("****** Trigger any process **", kwargs)


def verify_account(model, *args, **kwargs):
    print("verify account", args)
    print("verify account", kwargs)


def approve_account(*args, **kwargs):
    print("approve account")


def reject_account(*args, **kwargs):
    print("reject account")
