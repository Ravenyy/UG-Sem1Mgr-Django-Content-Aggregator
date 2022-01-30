from django.db import models


# Create your models here.

class Subject(models.Model):
    subject = models.CharField(max_length=255)
    image = models.FilePathField(path="/img")
    link = models.URLField(max_length=255)


class CovidContent(models.Model):
    headline = models.CharField(max_length=300)
    text = models.TextField()
    url = models.TextField()

    def __str__(self):
        return self.headline


class GamingContent(models.Model):
    headline = models.CharField(max_length=300)
    text = models.TextField()
    url = models.TextField()

    def __str__(self):
        return self.headline


class NewsContent(models.Model):
    headline = models.CharField(max_length=300)
    text = models.TextField()
    url = models.TextField()

    def __str__(self):
        return self.headline


class ProgrammingContent(models.Model):
    headline = models.CharField(max_length=300)
    text = models.TextField()
    url = models.TextField()

    def __str__(self):
        return self.headline


class ScienceContent(models.Model):
    headline = models.CharField(max_length=300)
    text = models.TextField()
    url = models.TextField()

    def __str__(self):
        return self.headline


class TechContent(models.Model):
    headline = models.CharField(max_length=300)
    text = models.TextField()
    url = models.TextField()

    def __str__(self):
        return self.headline


class Polskie(models.Model):
    headline = models.CharField(max_length=300)
    text = models.TextField()
    url = models.TextField()

    def __str__(self):
        return self.headline


class Swiat(models.Model):
    headline = models.CharField(max_length=300)
    text = models.TextField()
    url = models.TextField()

    def __str__(self):
        return self.headline
