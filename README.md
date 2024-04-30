# development

create venv

```sh
$ python3 -m venv citibike
```

then activate it

```sh
$ . ./citibike/bin/activate
```

install dependencies

```sh
$ pip install -r requirements.txt
```

run `maps.py` to generate/update maps. the maps will be saved to the `static` directory. start the development server using `$ flask --app wahoo run`

open [http://127.0.0.1:5000](http://127.0.0.1:5000) to view stuff!

---

# TODO

- refactor maps.py to use dictionary

## The project

This project is a visualization of CitiBike data from January 2023 developed by @exu3 and @eburlinson for CS1210 final project. link deployment and explain project further with screenshots.

## How to run locally

The project uses the following dependences which you can install with requirements.txt:

```
plotly
Flask
folium
```

Description of project is clear and concise 5
Description of division of labor and responsibilities among team members 5
Instructions for running / testing are clear 5
Estimate of project difficulty with justification of estimate 5
All dependencies / pip-installable modules clearly indicated 5
The program

Works as intended\* 40
Solution is decomposed into functions as appropriate 10
Program properly structured 10
Code is readable and concise 10
Total points: 100

- When evaluating your project, we will try to break your program, for example by supplying invalid data or responses at a prompt. Be sure your code handles such inputs gracefully!
