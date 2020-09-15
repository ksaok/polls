from django.db import models

# Create your models here.


class poll(models.Model):
    """Опрос"""
    name = models.CharField('Название', max_length=50)
    start_date = models.DateField('Дата начала')
    end_date = models.DateField('Дата окончания')
    description = models.TextField('Описание')

    def __str__(self):
        return f'Опрос "{self.name}"'

    class Meta:
        ordering = ['-start_date']
        verbose_name = ('Опрос')
        verbose_name_plural = ('Опросы')


class question(models.Model):
    """Вопрос"""
    poll = models.ForeignKey(poll, on_delete=models.CASCADE)
    question_types = [
        (0, 'Тектовый'),
        (1, 'Один вариант'),
        (2, 'Несколько вариантов')
    ]
    text = models.TextField('Текст вопроса')
    type = models.IntegerField(
        'Тип вопроса',
        choices=question_types,
        default=0
    )

    def __str__(self):
        return f'Вопрос №{self.id} ({self.poll.name})'

    class Meta:
        verbose_name = ('Вопрос')
        verbose_name_plural = ('Вопросы')


class choice(models.Model):
    """Варианты ответа"""
    question = models.ForeignKey(question, on_delete=models.CASCADE)
    name = models.CharField('Название', max_length=50)

    class Meta:
        verbose_name = ('Вариант')
        verbose_name_plural = ('Варианты')


class answer(models.Model):
    """Ответ пользователя"""
    question = models.ForeignKey(question, on_delete=models.CASCADE)
    choice = models.ForeignKey(choice, on_delete=models.CASCADE, null=True)
    user_id = models.IntegerField('ID пользователя')
    text = models.TextField('Текст ответа', null=True)

    class Meta:
        verbose_name = ('Ответ')
        verbose_name_plural = ('Ответы')
