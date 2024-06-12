from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    list_of_name_of_university = models.TextField(blank=True, null=True)
    invite_after_class = models.TextField(blank=True, null=True)
    invite_after_exams = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория ВУЗов'
        verbose_name_plural = 'Категории ВУЗов'


class Contacts(models.Model):
    site_url = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    time_table = models.TextField(blank=True, null=True)
    number = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

class Specialities(models.Model):
    name = models.TextField(blank=True, null=True)
    qualification = models.TextField(blank=True, null=True)
    cost = models.IntegerField(blank=True, null=True)
    places = models.IntegerField(blank=True, null=True)
    years_of_studying = models.IntegerField(blank=True, null=True)
    months_of_studying = models.IntegerField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'

class Pluses(models.Model):
    name = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Плюс'
        verbose_name_plural = 'Плюсы'

class University(models.Model):
    name = models.CharField(max_length=100)
    shortName = models.CharField(max_length=100)
    type = models.ForeignKey(Category, related_name='type_of_university', on_delete=models.SET_NULL, null=True, blank=True)
    list_of_pluses = models.ManyToManyField(Pluses, related_name='pluses', blank=True)
    places = models.IntegerField(blank=False, null=False, default=0)
    score = models.FloatField(blank=False, null=False, default=0)
    amount_of_specialities = models.IntegerField(blank=False, null=False, default=0)
    contacts = models.OneToOneField(Contacts, related_name="contacts", on_delete=models.SET_NULL, null=True, blank=True)
    specialities = models.ManyToManyField(Specialities, related_name='specialities', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ВУЗ'
        verbose_name_plural = 'ВУЗы'