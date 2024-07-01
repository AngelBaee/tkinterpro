import tkinter as tk
import webbrowser

def linkedin(event):
    webbrowser.open_new_tab('https://www.linkedin.com/in/mehrubon-sarimsakova-1a686a27b?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app')

def facebook(even):
    webbrowser.open_new_tab('https://www.facebook.com/emily.mcducan?mibextid=ZbWKwL') 

window = tk.Tk()
window.geometry("300x200")
window.title("Social Media Bookmark App")
label1 = tk.Label(text = "My Social Media")
label1.grid(column = 0, row = 0)

button1 = tk.Button(window, text = "Linkedin", bg ="orange")
button1.grid(column = 1, row = 1)
button2 = tk.Button(window,text ="Facebook", bg ="white")
button2.grid(column = 3, row = 1)

button1.bind("<Button-1>", linkedin)
button2.bind("<Button-1>", facebook)

window.mainloop()