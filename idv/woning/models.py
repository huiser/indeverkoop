from django.db import models


class Woning(models.Model):
    PROVINCIES = (
        ('GR', 'Groningen'),
        ('FR', 'Friesland'),
        ('DR', 'Drenthe'),
        ('OV', 'Overijssel'),
        ('FL', 'Flevoland'),
        ('GD', 'Gelderland'),
        ('UT', 'Utrecht'),
        ('NH', 'Noord-Holland'),
        ('ZH', 'Zuid-Holland'),
        ('ZL', 'Zeeland'),
        ('NB', 'Noord-Brabant'),
        ('LB', 'Noord-Brabant'),
    )
    LANDEN = (
        ('NL', 'Nederland'),
    )
    straat          = models.CharField(max_length=100)
    huisnummer      = models.CharField(max_length=10)
    plaats          = models.CharField(max_length=50)
    gemeente        = models.CharField(max_length=50)
    provincie       = models.CharField(max_length=5, choices=PROVINCIES, default='NL')
    land            = models.CharField(max_length=5, choices=LANDEN)
    created_at      = models.DateField(auto_now_add=True)
    modified_at     = models.DateField(auto_now=True)
    published_at    = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'woningen'
        ordering            = ['published_at', ]
