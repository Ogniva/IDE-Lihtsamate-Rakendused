import psutil
from tkinter import *

print("Total Ram:",psutil.virtual_memory()[0]/1024/1024/1024,"GB")
print("Available Ram:",psutil.virtual_memory()[1]/1024/1024/1024,"GB")
print("Percent Ram:",psutil.virtual_memory()[2],"%")
print("Used Ram:",psutil.virtual_memory()[3]/1024/1024/1024,"GB")
print("Free Ram:",psutil.virtual_memory()[4]/1024/1024/1024,"GB")
print("Cpu:", psutil.cpu_percent(), "%")

root = Tk()
root.title("RamCheck")
root.geometry("200x200")

poetry = "Total Ram:", round(psutil.virtual_memory()[0]/1024/1024/1024, 2),"GB"
label2 = Label(text=poetry, justify=LEFT)
label2.place(relx=.2, rely=.1)

poetry = "Available Ram:",round(psutil.virtual_memory()[1]/1024/1024/1024, 2),"GB"
label2 = Label(text=poetry, justify=LEFT)
label2.place(relx=.2, rely=.2)

poetry = "Percent Ram:",psutil.virtual_memory()[2],"%"
label2 = Label(text=poetry, justify=LEFT)
label2.place(relx=.2, rely=.3)

poetry = "Used Ram:",round(psutil.virtual_memory()[3]/1024/1024/1024, 2),"GB"
label2 = Label(text=poetry, justify=LEFT)
label2.place(relx=.2, rely=.4)

poetry = "Free Ram:",round(psutil.virtual_memory()[4]/1024/1024/1024, 2),"GB"
label2 = Label(text=poetry, justify=LEFT)
label2.place(relx=.2, rely=.5)

poetry = "Cpu:", psutil.cpu_percent(), "%"
label2 = Label(text=poetry, justify=LEFT)
label2.place(relx=.2, rely=.6)

root.mainloop()