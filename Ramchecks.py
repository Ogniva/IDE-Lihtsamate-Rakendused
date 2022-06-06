

import psutil

print("Total Ram:",psutil.virtual_memory()[0]/1024/1024/1024,"GB")
print("Available Ram:",psutil.virtual_memory()[1]/1024/1024/1024,"GB")
print("Percent Ram:",psutil.virtual_memory()[2],"%")
print("Used Ram:",psutil.virtual_memory()[3]/1024/1024/1024,"GB")
print("Free Ram:",psutil.virtual_memory()[4]/1024/1024/1024,"GB")
