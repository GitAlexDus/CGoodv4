from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#class User(models.Model): // activer aussi pour les resa

class Placard(models.Model):
    PlaNom = models.CharField(max_length=200)
    #PlaAdress = models.CharField(max_length=200)
    PlaPhoto = models.CharField(max_length=200, null=True, blank=True)
    #PlaMqttTopRacine = models.CharField(max_length=200)
    #PlaRef = models.CharField(max_length=5)
    #PlaTypeGateWay = models.CharField(max_length=200)
    #PlaTelNumber = models.CharField(max_length=200)
    #PlaCbType = models.CharField(max_length=200)
    PlaRqtStatusCode = models.CharField(max_length=200, null=True, blank=True)
    PlaOpenAllCode = models.CharField(max_length=200, null=True, blank=True)
    #PlaGerantDetails = models.CharField(max_length=200)
    PlaComment = models.TextField(null=True, blank=True)
    PlaStatus = models.BooleanField(default=False)
    def __str__(self):
        return self.PlaNom

 
class Casier(models.Model):
    placard = models.ForeignKey(Placard, on_delete=models.PROTECT)
    #CasRef = models.CharField(max_length=200) 
    CasNum = models.PositiveIntegerField()
    #objet  = models.OneToOneField(Objet, on_delete=models.PROTECT)
    CasObj = models.CharField(max_length=200)
    CasStatus = models.BooleanField(default=False)
    CasTaille = models.CharField(max_length=200)
    CasRqtStatusCode = models.CharField(max_length=200)
    CasOpenCode = models.CharField(max_length=200)
    CasComment = models.TextField(null=True, blank=True)
    CasMqttTopic = models.CharField(max_length=200)
    def __int__(self):
        return self.id
    
  

class Resa(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    #placad = models.ForeignKey(Casier, on_delete=models.PROTECT)
    casier  = models.ForeignKey(Casier, on_delete=models.PROTECT)
    #ResRef = models.CharField(max_length=200)
    ResDate = models.DateField('Date de la reservation - AAAA-MM-JJ')
    ResHeure = models.TimeField('Heure de la reservation - HH:mm')
    ResNbreHeure = models.DurationField('Nbre of booked hours', default=1)
    ResPIN = models.CharField('PIN Code', max_length=200)
    ResStatus = models.PositiveIntegerField(default=1)
    #ResComment = models.TextField(null=True, blank=True)
    def __int__(self):
        return self.id
 