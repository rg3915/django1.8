install:
	pip install -r requirements.txt

migrate:
	./manage.py makemigrations
	./manage.py migrate

createuser:
	./manage.py createsuperuser --username='admin' --email=''

shell_distributors:
	./manage.py shell < shell/distributors.py

shell_categorys:
	./manage.py shell < shell/categorys.py

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

script_echo:
	echo "<html><body><h1>Tutorial Django</h1><h3>Bem vindo ao Grupy-SP</h3></body></html>" > core/templates/index.html

create_template:
	mkdir core/templates/core
	touch core/templates/base.html
	touch core/templates/menu.html
	touch core/templates/core/movie_list.html
	touch core/templates/core/movie_detail.html
	touch core/templates/core/movie_form.html

initial: install migrate createuser load
