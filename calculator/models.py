from django.db import models

class Expressions(models.Model):
    # expression_id = models.ForeignKey(User, on_delete=models.CASCADE)
    expression_id = models.IntegerField(primary_key = True)
    expression = models.CharField('Формула',max_length=100)
    value = models.CharField('Значения',max_length=100)
    result = models.IntegerField("Результат", null=True)

    def __str__(self):
        return f'{self.expression}'

    class Meta:
        verbose_name = 'Формула'
        verbose_name_plural = "Формулы"
