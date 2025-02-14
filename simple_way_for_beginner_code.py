from meta_ai_api import MetaAI

def get_weather_info(country_name: str) -> str:
    llm = MetaAI()
    
    prompt = f"""You are custom gpt you have to tell about the weather of any country/city if the user asked 
        user asked for {country_name}
        you have to tell the weather of the country in the following format:
        - Temperature: 20°C
        - Weather: Sunny
        - Wind: 10 km/h
        - Humidity: 50%
        - Precipitation: 0 mm
        - Cloud cover: 50%
        - Wind direction: North
        - Wind speed: 10 km/h
        - Visibility: 10 km
        - Pressure: 1000 hPa
        - Dew point: 10°C
        - UV index: 10
        - Sunrise: 06:00
        - Sunset: 18:00
        - Moon phase: Full moon
        - Moon illumination: 100%

        and if the user asked something else you have to tell that you are not able to provide that information
    """
    
    response = llm.prompt(prompt)
    return response["message"]

if __name__ == "__main__":
    country_name = input("Enter the country/city name: ")
    if country_name:
        print("\nFetching weather information...\n")
        weather_info = get_weather_info(country_name)
        print("Weather Information:\n")
        print(weather_info)
    else:
        print("Please enter a country name!")
