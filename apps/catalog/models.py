from django.db import models


class Region(models.Model):
    name = models.CharField("Nomi", max_length=100, unique=True)
    slug = models.SlugField("Slug", max_length=120, unique=True)

    class Meta:
        verbose_name = "Viloyat"
        verbose_name_plural = "Viloyatlar"
        ordering = ["name"]

    def __str__(self):
        return self.name

class District(models.Model):
    region = models.ForeignKey(
        Region,
        on_delete=models.PROTECT,
        related_name="districts",
        verbose_name="Viloyat",
    )
    name = models.CharField("Nomi", max_length=100)
    slug = models.SlugField("Slug", max_length=120)

    class Meta:
        verbose_name = "Tuman"
        verbose_name_plural = "Tumanlar"
        ordering = ["region__name", "name"]
        constraints = [
            models.UniqueConstraint(
                fields=["region", "name"],
                name="unique_district_name_per_region",
            ),
            models.UniqueConstraint(
                fields=["region", "slug"],
                name="unique_district_slug_per_region",
            ),
        ]

    def __str__(self):
        return f"{self.name} ({self.region.name})"

class Category(models.Model):
    name = models.CharField("Nomi", max_length=100, unique=True)
    slug = models.SlugField("Slug", max_length=120, unique=True)

    class Meta:
        verbose_name = "Soha"
        verbose_name_plural = "Sohalar"
        ordering = ["name"]

    def __str__(self):
        return self.name