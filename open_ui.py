import tkinter as tk
from tkinter import ttk

id_var = None
lat1_var = None
lon1_var = None
lat2_var = None
lon2_var = None
submitted_data = {}


def main():
    global id_var, lat1_var, lon1_var, lat2_var, lon2_var

    def submit():
        global submitted_data
        submitted_data = {
            "ID": id_var.get(),
            "Latitude 1": lat1_var.get(),
            "Longitude 1": lon1_var.get(),
            "Latitude 2": lat2_var.get(),
            "Longitude 2": lon2_var.get(),
        }
        print(submitted_data)
        root.destroy()

    root = tk.Tk()
    root.title("Basic Input UI")

    frame = ttk.Frame(root, padding=16)
    frame.grid(row=0, column=0, sticky="NSEW")

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    id_var = tk.StringVar()
    lat1_var = tk.StringVar()
    lon1_var = tk.StringVar()
    lat2_var = tk.StringVar()
    lon2_var = tk.StringVar()

    ttk.Label(frame, text="ID:").grid(row=0, column=0, sticky="W", pady=4)
    ttk.Entry(frame, textvariable=id_var, width=30).grid(row=0, column=1, pady=4)

    ttk.Label(frame, text=" Starting Latitude:").grid(row=1, column=0, sticky="W", pady=4)
    ttk.Entry(frame, textvariable=lat1_var, width=30).grid(row=1, column=1, pady=4)

    ttk.Label(frame, text=" Starting Longitude:").grid(row=2, column=0, sticky="W", pady=4)
    ttk.Entry(frame, textvariable=lon1_var, width=30).grid(row=2, column=1, pady=4)

    ttk.Label(frame, text=" Destination Latitude:").grid(row=3, column=0, sticky="W", pady=4)
    ttk.Entry(frame, textvariable=lat2_var, width=30).grid(row=3, column=1, pady=4)

    ttk.Label(frame, text=" Destination Longitude:").grid(row=4, column=0, sticky="W", pady=4)
    ttk.Entry(frame, textvariable=lon2_var, width=30).grid(row=4, column=1, pady=4)

    ttk.Button(frame, text="Submit", command=submit).grid(row=5, column=0, columnspan=2, pady=12)


    root.mainloop()