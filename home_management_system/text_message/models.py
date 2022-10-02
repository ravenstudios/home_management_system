# from django.db import models
# from twilio.rest import Client
#
#
# # Create your models here.
# from django.db import models
#
# #defining a simple class
# class Text_Messaege(models.Model):
#
#     #save method
#     def save(self, *args, **kwargs):
#
#         #twilio code
#         account_sid = 'YOUR_ACCOUNT_SID'
#         auth_token = 'YOUR_AUTH_TOKEN'
#         client = Client(account_sid, auth_token)
#
#         message = client.messages.create(
#                                     body=f'',
#                                     from_='YOUR_TRIAL_NUMBER',
#                                     to='VERIFIED_NUMBER'
#                                 )
#
#         print(message.sid)
#         return super().save(*args, **kwargs)
#
#     #string representation
#     def __str__(self):
#         return str(self.test_result)
