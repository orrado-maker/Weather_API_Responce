import tkinter as tk
import api_request
import comparisonLogic


def main():
    root = tk.Tk()
    root.title("Comparison Results")

    # Single-line text box (Entry)
    #entry1 = tk.Entry(root, width=40)
    #entry1.pack(padx=10, pady=5)

    #entry2 = tk.Entry(root, width=40)
    #entry2.pack(padx=10, pady=5)

    # Multi-line text box (Text)
    text_box = tk.Text(root, width=80, height=20)
    text_box.pack(padx=10, pady=5)
    


    # Get API data
    data1 = api_request.api_request1()
    if data1:
        temp1 = data1["current_weather"]["temperature"]
    else:
        text_box.insert(tk.END, "Failed to retrieve data1\n")
        return
    
    data2 = api_request.api_request2()
    if data2:
        temp2 = data2["current_weather"]["temperature"]
    else:
        text_box.insert(tk.END, "Failed to retrieve data2\n")
        return

    # Compare
    result = comparisonLogic.compare_api_responses(temp1, temp2)
    text_box.insert(tk.END, result + "\n")
    
    if comparisonLogic.isCold == 1:
        #text_box.insert(tk.END, "Location 1 is colder than Location 2.\n")
        text_box.insert(tk.END, f"Your starting location is warmer than your destination by {comparisonLogic.tempDifference} degrees.\nYou should consider taking a jacket or a longsleeve shirt.\n")
    elif comparisonLogic.isWarm == 1:
        #text_box.insert(tk.END, "Location 2 is colder than Location 1.\n")
        text_box.insert(tk.END, f"Your starting location is colder than your destination by {comparisonLogic.tempDifference} degrees.\nYou should consider taking a hoodie or a light jacket.\n")
        #text_box.insert(tk.END, "You should consider taking a hoodie or a light jacket.\n")
    else:
        #text_box.insert(tk.END, "Location 1 and Location 2 have the same temperature.\n")
        #text_box.insert(tk.END, "Your starting location and destination have the same temperature.\n")
        text_box.insert(tk.END, "You should bring what you normally bring.\n")
    if comparisonLogic.isWindy == 1:
        text_box.insert(tk.END, "Your starting location is windier than your destination.\n")
    elif comparisonLogic.isWindy == -1:
        text_box.insert(tk.END, "Your destination is windier than your starting location.\n")
    else: 
        pass
    root.mainloop()