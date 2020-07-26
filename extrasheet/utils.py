import datetime
from django.utils import timezone

from django.contrib.contenttypes.models import ContentType
from .models import Notify
def create_notify(user, verb,target=None):
    now = timezone.now()
    last_minute = now - datetime.timedelta(seconds=60)
    similar_notify = Notify.objects.filter(user_id=user.id,verb=verb,created__gte=last_minute)
    
    if target:
        target_ct = ContentType.objects.get_for_model(target)
        similar_notify = similar_notify.filter(
        target_ct=target_ct,
        target_id=target.id)
    if not similar_notify:
        notify = Notify(user=user, verb=verb, target=target)
        notify.save()
        return True
    return False