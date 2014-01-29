from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.contrib.auth.models import User
from django_countries.fields import CountryField


LANDEN = (
    ('NL', 'Nederland'),
)

class Profiel(models.Model):
    GESLACHT_CHOICES = (
        ('M', 'Man'),
        ('V', 'Vrouw'),
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='profiel',
        unique=True
    )
    geslacht = models.CharField(
        max_length=1,
        choices=GESLACHT_CHOICES,
    )
    voorletters = models.CharField(
        max_length=20,
    )
    roepnaam = models.CharField(
        max_length=50,
        blank=True,
    )
    tussenvoegsel = models.CharField(
        max_length=20,
        blank=True,
    )
    achternaam = models.CharField(
        max_length=50,
    )
    telefoonnummer1 = models.CharField(
        'telefoonnummer 1',
        max_length=20,
        blank=True,
    )
    telefoonnummer2 = models.CharField(
        'telefoonnummer 2',
        max_length=20,
        blank=True,
    )
    post_straat = models.CharField(
        'straat',
        max_length=100,
        blank=True,
    )
    post_huisnummer = models.CharField(
        'huisnummer',
        max_length=10,
        blank=True,
    )
    post_toevoeging = models.CharField(
        'huisnr toev.',
        max_length=10,
        blank=True,
    )
    post_postcode = models.CharField(
        'postcode',
        max_length=10,
        blank=True,
    )
    post_plaats = models.CharField(
        'plaats',
        max_length=50,
        db_index=True
    )
    post_land = CountryField(
        'land', 
        default='NL',
    )

    class Meta:
        verbose_name_plural = 'profielen'

    def __str__(self):
        tussenvoegsel = ''
        roepnaam = ''
        if self.tussenvoegsel:
            tussen = ' %s' % self.tussenvoegsel
        if self.roepnaam:
            roepnaam = ' (%s)' % self.roepnaam
        return '%s%s %s%s' % (self.voorletters, tussenvoegsel, self.achternaam, roepnaam)

    def volledigenaam(self):
        tussenvoegsel = ''
        roepnaam = ''
        if len(self.tussenvoegsel) > 0:
            tussenvoegsel = ' %s' % self.tussenvoegsel
        if len(self.roepnaam) > 0:
            roepnaam = ' (%s)' % self.roepnaam
        return '%s%s %s%s' % (self.voorletters, tussenvoegsel, self.achternaam, roepnaam)

    def get_absolute_url(self):
        return reverse('profiel')


#class IdvUserManager(BaseUserManager):
#    def create_user(self, email, password=None):
#        """
#        Creates and saves a User with the given email and password.
#        """
#        if not email:
#            msg = "Users must have an email address"
#            raise ValueError(msg)
#
#        user = self.model(
#            email=IdvUserManager.normalize_email(email)
#        )
#        user.set_password(password)
#        user.save(using=self._db)
#        return user
#
#    def create_superuser(self, email, password):
#        """
#        Creates and saves a superuser with the given email and password.
#        """
#        user = self.create_user(email,
#            password=password,
#        )
#        user.is_admin = True
#        user.is_staff = True
#        user.is_superuser = True
#        user.save(using=self._db)
#        return user


#class IdvUser(AbstractBaseUser, PermissionsMixin):
#    """ Inherits from both the AbstractBaseUser and PermissionMixin. """
#
#    GESLACHT_CHOICES = (
#        ('M', 'Man'),
#        ('V', 'Vrouw'),
#    )
#
#    email = models.EmailField(
#        verbose_name="email adres",
#        max_length=50,
#        unique=True,
#        db_index=True,
#    )
#    actief = models.BooleanField(
#        _('Actief'),
#        default=True,
#    )
#    is_staff = models.BooleanField(
#        _('Beheerder'),
#        default=False,
#    )
#    voorletters = models.CharField(
#        max_length=20,
#    )
#    roepnaam = models.CharField(
#        max_length=50,
#        blank=True,
#    )
#    tussenvoegsel = models.CharField(
#        max_length=20,
#        blank=True,
#    )
#    achternaam = models.CharField(
#        max_length=50,
#    )
#    geslacht = models.CharField(
#        max_length=1,
#        choices=GESLACHT_CHOICES,
#    )
#    telefoonnummer1 = models.CharField(
#        max_length=20,
#        blank=True,
#    )
#    telefoonnummer2 = models.CharField(
#        max_length=20,
#        blank=True,
#    )
#
#    USERNAME_FIELD = "email"
#    REQUIRED_FIELDS = ['voorletters', 'achternaam',]
#
#    objects = IdvUserManager()
#
#    def get_full_name(self):
#        if length(self.tussenvoegsel):
#            return "%s %s %s" % (
#                self.voorletters,
#                self.tussenvoegsel,
#                self.achternaam
#            )
#        else:
#            return "%s %s" % (
#                self.voorletters,
#                self.achternaam
#            )
#
#    def get_short_name(self):
#        return self.email
#
#    def __unicode__(self):
#        return self.email
#
#    def __str__(self):
#        return self.email
