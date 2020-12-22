#===========================
# Imports
#===========================
import tkinter as tk
from tkinter import ttk, colorchooser as cc, Menu, Spinbox as sb, scrolledtext as st, messagebox as mb, filedialog as fd, simpledialog as sd

import requests
import time

#===========================
# Main App
#===========================
class App(tk.Tk):
    """Main Application."""
    #------------------------------------------
    # Initializer
    #------------------------------------------
    def __init__(self):
        super().__init__()
        self.init_config()
        self.init_vars()
        self.init_widgets()
        self.init_events()

    #------------------------------------------
    # Instance Variables
    #------------------------------------------
    def init_vars(self):
        self.small_font = ('Arial', 15, 'bold')
        self.large_font = ('Arial', 35, 'bold')

    #-------------------------------------------
    # Window Settings
    #-------------------------------------------
    def init_config(self):
        self.resizable(True, True)
        self.title('Weather Application Version 1.0')
        self.iconbitmap('python.ico')
        self.style = ttk.Style(self)
        self.style.theme_use('clam')

    #-------------------------------------------
    # Window Events / Keyboard Shorcuts
    #-------------------------------------------
    def init_events(self):
        self.entry.bind('<Return>', self.get_weather)

    #-------------------------------------------
    # Widgets / Components
    #-------------------------------------------
    def init_widgets(self):

        frame = ttk.Frame(self)
        frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        fieldset = ttk.LabelFrame(frame, text='Enter City Location')
        fieldset.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.location = tk.StringVar()
        self.entry = ttk.Entry(fieldset, width=20, textvariable=self.location, font=self.large_font)
        self.entry.pack(fill=tk.X, expand=True)
        self.entry.focus()

        self.final_info = ttk.Label(frame, font=self.large_font)
        self.final_info.pack(fill=tk.X, expand=True, padx=10, pady=10)
        self.final_data = ttk.Label(frame, font=self.small_font)
        self.final_data.pack(fill=tk.X, expand=True, padx=10, pady=10)
        self.final_info.pack_forget()
        self.final_data.pack_forget()

    # ------------------------------------------
    def get_weather(self, event):
        location = self.location.get()
        key = 'bfa44522970d958fbbe855209b7f3772'
        api = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={key}'
        json_data = requests.get(api).json()

        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp'] - 273.15)
        min_temp = int(json_data['main']['temp_min'] - 273.15)
        max_temp = int(json_data['main']['temp_max'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600)) # - 6 hours
        sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600)) # - 6 hours

        final_info = f'Condition: {temp} °C'
        final_data = f'''
        Max temperature: {max_temp}
        Min temperature: {min_temp}
        Pressure: {pressure}
        Humidity: {humidity}
        Wind Speed: {wind}
        Sunrise: {sunrise}
        Sunset: {sunset}
        '''

        self.final_info.config(text=final_info)
        self.final_data.config(text=final_data)
        self.final_info.pack(fill=tk.X, expand=True, padx=10, pady=10)
        self.final_data.pack(fill=tk.X, expand=True, padx=10, pady=10)

#===========================
# Start GUI
#===========================
def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()