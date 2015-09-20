# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse_lazy


class Distributor(models.Model):
    distributor = models.CharField('distribuidor', max_length=50, unique=True)

    class Meta:
        ordering = ['distributor']
        verbose_name = 'distribuidor'
        verbose_name_plural = 'distribuidores'

    def __str__(self):
        return self.distributor


class Category(models.Model):
    category = models.CharField('categoria', max_length=50, unique=True)

    class Meta:
        ordering = ['category']
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.category


class Movie(models.Model):
    movie = models.CharField('filme', max_length=100)
    category = models.ForeignKey(
        'Category', verbose_name='categoria', related_name='movie_category')
    distributor = models.ForeignKey(
        'Distributor', verbose_name='distribuidor', related_name='movie_distributor')
    raised = models.DecimalField('arrecadou', max_digits=4, decimal_places=3)
    liked = models.BooleanField('gostou', default=True)
    release = models.DateTimeField(u'lançamento')

    class Meta:
        ordering = ['-release']
        verbose_name = 'filme'
        verbose_name_plural = 'filmes'

    def __str__(self):
        return self.movie

    def get_absolute_url(self):
        return reverse_lazy('movie_detail', kwargs={'pk': self.pk})
