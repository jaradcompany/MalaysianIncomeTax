from tkinter import *

class HR:    
    class System:
        def __init__(self, version, application):
            self.title = application
            self.window = Tk()
            self.menu = Menu(self.window)
        
        def about(self):
            nwindow = Toplevel(self.window)
            nwindow.title("About Developer")
            nwindow.geometry("400x200")
            
            Label(nwindow, text="This application is developed by John Melody Me").pack()
            
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
        