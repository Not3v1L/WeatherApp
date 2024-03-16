% rebase('layout.tpl', title=title, year=year)

<h2>{{ title }}.</h2>
<img src="{{weather.weather.value}}"></img>
<h3>Погода днем {{weather.day_temperature}}</h3>
<h3>Погода ночью {{weather.night_temperature}}</h3>