import time
import win10toast
a = str(input("For what you want me to remined you ? : "))
b = float(input("By what time in minutes you want me to remined you ? : "))
b = b*60
time.sleep(b)
print(a)
from win10toast import ToastNotifier
n = ToastNotifier()
# enter time in minutes
n.show_toast(f"Time for {a}")
duration = b 
icon_path = ("https://media.geeksforgeeks.org/wp-content/uploads/geeks.ico")

