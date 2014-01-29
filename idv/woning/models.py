from django.db import models
from django.conf import settings


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
    verkoper        = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    straat          = models.CharField(max_length=100)
    huisnummer      = models.CharField(max_length=10)
    plaats          = models.CharField(max_length=50, db_index=True)
    gemeente        = models.CharField(max_length=50, db_index=True)
    provincie       = models.CharField(max_length=5, choices=PROVINCIES, default='NL', db_index=True)
    land            = models.CharField(max_length=5, choices=LANDEN, db_index=True)
    created_at      = models.DateField(auto_now_add=True, db_index=True)
    modified_at     = models.DateField(auto_now=True, db_index=True)
    published_at    = models.DateField(null=True, blank=True, db_index=True)

    class Meta:
        verbose_name_plural = 'woningen'
        ordering            = ['published_at', ]

    def __unicode__(self):
        return u"%s %s, %s" % (self.straat, self.huisnummer, self.plaats)
