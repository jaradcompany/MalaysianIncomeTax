import webbrowser
from tkinter import *
from PIL import Image, ImageTk

class HR:    
    class System:
        def __init__(self, version, application):
            self.devlinkedin = "https://www.linkedin.com/in/johnmelodyme/"
            self.source = "https://github.com/justanotherresearchanddevelopment/HrSystem"
            self.title = application
            self.window = Tk()
            self.menu = Menu(self.window)
        
        def about(self):
            def dev(): webbrowser.open_new_tab(self.devlinkedin)
            def source(): webbrowser.open_new_tab(self.source)
                
            nwindow = Toplevel(self.window)
            nwindow.title("About Developer")
            nwindow.geometry("400x200")
            nwindow.resizable(False, False)
            nwindow.configure(bg="white")
            
            image = ImageTk.PhotoImage(Image.open("assets/jarad.png").resize((0x64, 0x64), Image.ANTIALIAS))
            logo = Label(nwindow, image=image, anchor=CENTER)
            logo.image = image
            logo.pack(pady=0xA)
            
            Label(nwindow, text="This application is developed by JARAD Company", bg="white").pack()
            Button(nwindow, text="Visit Developer's profile", command=dev, bg="white", bd=0x0, fg="blue").pack(pady=0x5)
            Button(nwindow, text="Source", command=source, bg="white", bd=0x0, fg="blue").pack(pady=0x3)
            
        def setMenuBar(self):
            # _FILE_
            file_menu = Menu(self.menu, tearoff=0x0)
            file_menu.add_command(label="Save as PDF", command=self.printToPdf)
            file_menu.add_command(label="Exit", command=self.exit)
            
            # __ABOUT__
            about_menu = Menu(self.menu, tearoff=0x0)
            about_menu.add_command(label="About Developer", command=self.about)
            
            self.menu.add_cascade(label="File", menu=file_menu)
            self.menu.add_cascade(label="Help", menu=about_menu)
            self.window.config(menu=self.menu)
            
        def exit(self): self.window.destroy()
        
        def printToPdf(self): pass
        
        def run(self):
            # Set the window's size
            self.window.geometry("1200x600+50+50")
            # Set icon for the window
            self.window.iconbitmap(self.window, 'assets/app.ico')
            # Set title for the window
            self.window.title(self.title)
            # Set Menu bar
            self.setMenuBar()
            # Execute the window
            self.window.mainloop()
        
if __name__ == "__main__":
    hr = HR().System(version=1.0, application="HR System")
    hr.run()
        