from .models import Page
from django.db.models.signals import post_delete
from django.dispatch import receiver

@receiver(post_delete,sender=Page)
def delete_releted_user(sender,instance,**kwargs):
    print("Post post_delete!!!")
    instance.user.delete()