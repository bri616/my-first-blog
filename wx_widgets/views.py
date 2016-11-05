import requests

from django.shortcuts import render


# Create your views here.
def widget_list(request):
    api_key = "74062f6cda3833e314188a373291671c"
    city = 'Seattle'
    request_url = 'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={api_key}'.format(
        city=city,
        api_key=api_key
    )
    current_wx_data = requests.get(request_url)
    wx_json = current_wx_data.json()
    # import ipdb; ipdb.set_trace()
    return render(request, 'wx_widgets/widget_list.html', {'wx_json': wx_json})
