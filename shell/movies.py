from core.models import Distributor, Category, Movie
import datetime
category = Category.objects.get(category='aventura')
distributor = Distributor.objects.get(distributor__icontains='line')
Movie.objects.create(
    movie='O Senhor dos Anéis: O Retorno do Rei',
    category=category,
    distributor=distributor,
    raised=1.119,
    release=datetime.date(2003, 12, 25)
)
category = Category.objects.get(category='ação')
distributor = Distributor.objects.get(distributor__icontains='disney')
Movie.objects.create(
    movie='Homem de Ferro 3',
    category=category,
    distributor=distributor,
    raised=1.215,
    release=datetime.date(2013, 4, 26)
)
category = Category.objects.get(category='ação')
distributor = Distributor.objects.get(distributor__icontains='disney')
Movie.objects.create(
    movie='Os Vingadores',
    category=category,
    distributor=distributor,
    raised=1.519,
    release=datetime.date(2012, 4, 27)
)
category = Category.objects.get(category='aventura')
distributor = Distributor.objects.get(distributor__icontains='paramount')
Movie.objects.create(
    movie='Titanic',
    category=category,
    distributor=distributor,
    raised=2.186,
    release=datetime.date(1998, 1, 16)
)
category = Category.objects.get(category='aventura')
distributor = Distributor.objects.get(distributor__icontains='fox')
Movie.objects.create(
    movie='Avatar',
    category=category,
    distributor=distributor,
    raised=2.787,
    release=datetime.date(2009, 11, 18)
)
category = Category.objects.get(category='guerra')
distributor = Distributor.objects.get(distributor__icontains='warner')
Movie.objects.create(
    movie='300',
    category=category,
    distributor=distributor,
    raised=0.456,
    release=datetime.date(2007, 3, 30)
)
