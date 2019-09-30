import requests, json 
import argparse 


def get_forecast(zip=560064,today=None):
      
    # Enter your API key here 
    api_key = "64315ebd079846c4b15ebd079806c408"
     
    # Give city name 
    pincode = str(zip)

    # base_url variable to store url 
    url = "https://api.weather.com/v3/wx/forecast/daily/5day?postalKey="+pincode+":IN&units=e&language=en-US&format=json&apiKey="+api_key

    response = requests.get(url,verify=False) 

    # python format data 
    x = response.json()
    if !today():
        today = x['dayOfWeek'][0]
    elif today.capitalize() in x['dayOfWeek']:       
        today = today
    else:
        print('Day name incorrect or not found')
        exit(0)
        
    index = x['dayOfWeek'].index(today)
    indx = index*2
    Text = 'On '+x['sunriseTimeLocal'][index]+' '+x['dayOfWeek'][index]\
        +' minimum temperature will be '+str(x['temperatureMin'][index])+' Deg. Farenheit'\
        +' and maximum temperature will be '+str(x['temperatureMax'][index])+' Deg. Farenheit'\
        +'. '+x['narrative'][index]+'. ' \    
        +' \n'+str(x['daypart'][0]['daypartName'][indx])\
        +' \nCloud cover :- '+str(x['daypart'][0]['cloudCover'][indx])\
        +' \nPrecipitation type :- '+str(x['daypart'][0]['precipType'][indx])\
        +' \nRelative Humidity :- '+str(x['daypart'][0]['relativeHumidity'][indx])\
        +' \nTemperature :- '+str(x['daypart'][0]['temperature'][indx])+' Deg. Farenheit'\
        +' \nThunder Category :- '+x['daypart'][0]['thunderCategory'][indx]\
        +' \nSummary :- '+x['daypart'][0]['narrative'][indx] 
    
    return Text
    
 
def main(): 
  
    parser = argparse.ArgumentParser(prog ='weather', 
                                     description ='Command to get weather day wise') 
  
    parser.add_argument('zip', metavar ='N', type = int, nargs ='+', 
                        help ='the zip code of the area for which weather has to be extracted') 
    parser.add_argument('-day', action ='store_const', const = True, 
                        default = 'Today', dest ='greet', 
                        help ="Extract weather of which day.") 
  
    args = parser.parse_args() 
  
    print(get_forecast(args.zip,args.day))



