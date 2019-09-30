from myPackage import weather

def test_forecast():
    '''
    get forecast for Bengaluru 560074
    '''
    day = 'Monday'
    zip = 560064
    returned_forecast = weather.get_forecast(zip,day)
    print(returned_forecast)
    