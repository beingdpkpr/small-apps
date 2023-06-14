from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from tkinter import Tk, mainloop, PhotoImage

# Window UI Setup
root = Tk()
root.title('Weather App')
root.geometry('890x470+300+300')
root.configure(bg='#070110')
root.resizable(False, False)

# Icon
imageIcon = PhotoImage(file='assets/dpkpr_logo.png')
root.iconphoto(False, imageIcon)


if __name__ == '__main__':
    mainloop()
