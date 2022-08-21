from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class FamilyMember(models.Model):
    name = models.CharField(max_length=20, default=0)
    image = models.ImageField(blank=True, null=True, upload_to='user_images')
    phone_number = models.CharField(max_length=20, default=0)

    def __str__(self):
        return self.name


        

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to='user_images') # or whatever
    test = models.CharField(max_length=20, default=0)


    def __str__(self):
        return self.user.username

    #
    # def get_image(self):
    #     return {self.image}
    #
    #
    # def get_test(self):
    #     return {self.test}


    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)
    #
    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()



    # # Override the save method of the model
    # def save(self):
    #     super().save()
    #
    #     img = Image.open(self.image.path) # Open image

        # # resize image
        # if img.height > 300 or img.width > 300:
        #     output_size = (300, 300)
        #     img.thumbnail(output_size) # Resize image
        #     img.save(self.image.path) # Save it again and override the larger image
