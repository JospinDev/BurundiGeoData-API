from django.db import models

class Province(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=10, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Commune(models.Model):
    province = models.ForeignKey(Province, related_name='communes', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        unique_together = ('province', 'name')

    def __str__(self):
        return f"{self.name} ({self.province})"


class Zone(models.Model):
    commune = models.ForeignKey(Commune, related_name='zones', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ('commune', 'name')

    def __str__(self):
        return f"{self.name} ({self.commune})"


class Quartier(models.Model):
    zone = models.ForeignKey(Zone, related_name='quartiers', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ('zone', 'name')

    def __str__(self):
        return f"{self.name} ({self.zone})"
