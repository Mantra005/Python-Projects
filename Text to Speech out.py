# to install win32com.client in windows, run script in shll : pip install win32.client
import win32com.client

a = input("Enter the text to speech out : ")
speaker = win32com.client.Dispatch("SAPI.SpVoice") 
# you can change the voice by changing through system
speaker.Speak(a)
 
