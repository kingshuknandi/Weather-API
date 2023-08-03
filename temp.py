import requests

API_BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
def get_weather_data():
    response = requests.get(API_BASE_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data. Please try again.")
        return None

def get_temperature(data, date):
    for entry in data['list']:
        if entry['dt_txt'] == date:
            return entry['main']['temp']
    return None

def get_wind_speed(data, date):
    for entry in data['list']:
        if entry['dt_txt'] == date:
            return entry['wind']['speed']
    return None

def get_pressure(data, date):
    for entry in data['list']:
        if entry['dt_txt'] == date:
            return entry['main']['pressure']
    return None
def main():
    data = get_weather_data()
    if data is None:
        return

    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            temperature = get_temperature(data, date)
            if temperature is not None:
                print(f"Temperature at {date}: {temperature} K")
            else:
                print("Date not found in the forecast.")

        elif choice == '2':
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            wind_speed = get_wind_speed(data, date)
            if wind_speed is not None:
                print(f"Wind speed at {date}: {wind_speed} m/s")
            else:
                print("Date not found in the forecast.")

        elif choice == '3':
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS): ")
            pressure = get_pressure(data, date)
            if pressure is not None:
                print(f"Pressure at {date}: {pressure} hPa")
            else:
                print("Date not found in the forecast.")

        elif choice == '0':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
