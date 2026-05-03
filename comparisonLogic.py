import api_request



isCold = 0
isWarm = 0
isWindy = 0
tempDifference =0

def compare_api_responses(temp1, temp2):
    global isCold, isWarm, tempDifference
    tempDifference = temp1 - temp2
    if temp1 > temp2:
        isCold = 1
        isWarm = 0
        tempDifference = round(abs(temp1 - temp2),2)
        return "Location 1 is warmer than Location 2."
    elif temp1 < temp2:
        isWarm = 1
        isCold = 0
        tempDifference = round(abs(temp2 - temp1),2)
        return "Location 2 is warmer than Location 1."
    else:
        isCold = 0
        isWarm = 0
        tempDifference = 0
        return "Location 1 and Location 2 have the same temperature."
        

def compare_wind_speed(wind_speed1, wind_speed2):
    if wind_speed1 > wind_speed2:
        isWindy += 1
        return "Location 1 is windier than Location 2."
    elif wind_speed1 < wind_speed2:
        isWindy += -1
        return "Location 2 is windier than Location 1."
    else:
        #return "Location 1 and Location 2 have the same wind speed."
        pass
       # return "Location 1 and Location 2 have the same wind speed."



def maincompare():
    data1 = api_request.api_request1()
    data2 = api_request.api_request2()

    if not data1 or not data2:
        print("Failed to retrieve both API responses.")
        return

    temp1 = data1["current_weather"]["temperature"]
    temp2 = data2["current_weather"]["temperature"]

    #print(f"Temp1: {temp1}")
    #print(f"Temp2: {temp2}")
    print(compare_api_responses(temp1, temp2))


if __name__ == "__main__":
    maincompare()


