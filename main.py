import datetime # for reading present date
import time # for auto update
import requests # for fetching data from web
from plyer import notification # for notification on pc

covid_data = None

try:
    covid_data = requests.get("https://corona-rest-api.herokuapp.com/Api/india")
except:
    # if data not fetched due to some internet issues
    print('check your internet connection !')

# if we fetched the data
if covid_data != None:
    # convert data into JSON format
    data = covid_data.json()['Success']

    while True:
        notification.notify(
            # title of the notification
            title = 'COVID19 Stats on {}'.format(datetime.date.today()),
            # body of the notification
            message = 'Total cases : {totalcases}\nToday cases : {todaycases}\nToday deaths :{todaydeaths}\nTotal active :{active}\nCritical: {critical}'.format(
                        totalcases = data['cases'],
                        todaycases = data['todayCases'],
                        todaydeaths = data['todayDeaths'],
                        active = data['active'],
                        critical = data['critical']),
            # icon for the notification
            
            app_icon = 'covid_icon.ico',
            timeout = 10
        )
        # sleep for 12 hrs
        # time.sleep(12*60*60)
        break