install:
	pip install -r requirements.txt

migrate:
	./manage.py makemigrations
	./manage.py migrate

createuser:
	./manage.py createsuperuser --username='admin' --email=''

shell_distributors:
	./manage.py shell < shell/distributors.py

shell_movies:
	./manage.py shell < shell/movies.py

selenium_movie:
	python selenium/selenium_movie.py

backup:
	./manage.py dumpdata core --format=json --indent=2 > fixtures.json

load:
	./manage.py loaddata fixtures.json

run:
	./manage.py runserver

pdf:
	latexmk -pdf -shell-escape django_tutorial.tex

pvc:
	latexmk -pdf -shell-escape -pvc django_tutorial.tex

clear:
	latexmk -c
	rm *.nav *.snm *.vrb

initial: install migrate createuser load
