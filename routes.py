"""
Routes and views for the bottle application.
"""

from pdb import post_mortem
from bottle import route, view, request, post
from datetime import datetime
from enum import Enum
import json
import re

class Weather(Enum):
    CLOUDY = 'static\images\cloudy.png'
    SUNNY = 'static\images\sunny.png'

class CityWeather:
  def __init__(self, weather, day_temperature, night_temperature):
    self.weather = weather
    self.day_temperature = day_temperature
    self.night_temperature = night_temperature

cities = ["Санкт-Петербург", "Москва"]

city_to_weather = {"Санкт-Петербург" : CityWeather(Weather.CLOUDY, 5, -1),
                   "Москва" : CityWeather(Weather.SUNNY, 10, 2)}

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
    try:
        city_index = int(request.GET.get('city', '').strip())
        city = cities[city_index]
        return dict(
            title='Погода в городе: ' + city,
            message='',
            year=datetime.now().year,
            weather=city_to_weather[city]
        )
    except:
        return '<h1>Запрашиваемый город не найден</h1>'

@route('/orders')
@view('orders_view')
def orders():
    try: # Load existing data from JSON file if exists
        with open('orders_data.json', 'r') as f:
            orders = json.load(f)
    except FileNotFoundError:
        orders = {}

    return dict(
            orders = orders,
            title='Заказы',
            year=datetime.now().year
        )

@post('/orders', method='post')
def make_order_form_handler():
    phone_pattern = r'^8-\d{3}-\d{3}-\d{2}-\d{2}$'
    not_only_spaces_pattern = r'^\S.*\S$'
    
    
    
    print('hello world')
    product_name = request.forms.get('PRODUCT_NAME')
    description = request.forms.get('PRODUCT_DESCRIPTION')
    phone_number = request.forms.get('PHONE_NUMBER')
    
    if not phone_number:
        return "You have to fill in phone number field"
    elif not product_name:
        return "You have to fill in product name field"
    elif not description:
        return "You have to fill in description field"
    elif not re.fullmatch(phone_pattern, phone_number):
        return "Number has to be in 8-xxx-xx-xx format"
    elif not re.fullmatch(not_only_spaces_pattern, product_name):
        return "Product name cannot consist only of spaces"
    elif not re.fullmatch(not_only_spaces_pattern, description):
        return "Description cannot consist only of spaces"

    
    
    try: # Load existing data from JSON file if exists
        with open('orders_data.json', 'r') as f:
            orders = json.load(f)
    except FileNotFoundError:
        orders = {}
    
    if phone_number in orders:
        orders[phone_number].append((product_name, description))
    else:
        orders[phone_number] = [(product_name, description)]
    
    with open('orders_data.json', 'w') as f:
        json.dump(orders, f, indent=4)
    
    return "Thanks for the order! We will call you on %s in order to discuss the details." % (phone_number)
