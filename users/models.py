from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField('Фото пользователя', default='default.png', upload_to='user_images')

    def __str__(self):
        return f'Профаил пользователя {self.user.username}'

    def svae(self, *args, **kwards):
        super().save()

        image = Image.open(self.img.path)

        if image.hight > 256 or image.width > 256:
            resize = (256, 256)
            image.thumbnail(resize)
            image.save(self.img.path)

    class Meta:
        verbose_name = 'Профаил'
        verbose_name_plural = 'Профайлы'
