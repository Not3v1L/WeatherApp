"""
Routes and views for the bottle application.
"""

from bottle import route, view, request
from datetime import datetime

cities = ["Санкт-Петербург", "Москва"]

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year,
        cities=cities
    )

@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(
        title='Контакты',
        message='',
        year=datetime.now().year
    )

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='О нас',
        message='',
        year=datetime.now().year
    )

@route('/city_weather')
@view('city_weather')
def city_weather():
    city_index = int(request.GET.get('city', '').strip())
    return dict(
        title='Погода в городе: ' + cities[city_index],
        message='',
        year=datetime.now().year
    )
