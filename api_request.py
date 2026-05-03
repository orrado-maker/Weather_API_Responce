import return_ui
import open_ui
import requests


def api_request1():
    try:
        latitude = open_ui.submitted_data.get("Latitude 1")
        longitude = open_ui.submitted_data.get("Longitude 1")
        
        if not latitude or not longitude:
            print("Error: Latitude 1 or Longitude 1 not found in submitted data")
            return None
        
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
        response = requests.get(url)
        response.raise_for_status()
        global data1, temp1
        data1 = response.json()
        temp1 = data1["current_weather"]["temperature"]
        #print(temp1)
        return data1
 
    except Exception as e:
        print(f"API request 1 failed: {e}")
        return None

def api_request2():
    try:
        latitude = open_ui.submitted_data.get("Latitude 2")
        longitude = open_ui.submitted_data.get("Longitude 2")
        
        if not latitude or not longitude:
            print("Error: Latitude 2 or Longitude 2 not found in submitted data")
            return None
        
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
        response = requests.get(url)
        response.raise_for_status()
        global data2, temp2
        data2 = response.json()
        temp2 = data2["current_weather"]["temperature"]
        #print(temp2)
        return data2
    except Exception as e:
        print(f"API request 2 failed: {e}")
        return None