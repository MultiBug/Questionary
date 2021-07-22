from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Participants(models.Model):
    fullname = models.CharField(verbose_name='Ф.И.О.', max_length=128)
    sex_status = (
        (1, 'Мужской'),
        (2, 'Женский'),
        (3, 'Неопределенный'),
    )
    sex = models.IntegerField(verbose_name='Пол', choices=sex_status)
    marital_status = (
        (1, 'Замужем / Женат'),
        (2, 'Не замужем / Не женат'),
        (3, 'Раздельное проживание'),
        (4, 'Разведен(а)'),
        (5, 'Вдовец / Вдова'),
    )
    marital = models.IntegerField(verbose_name='Семейное Положение', choices=marital_status)
    nationality = models.CharField(verbose_name='Национальность', max_length=64)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

