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
            nwindow.resizable(width=False, height=False)
            nwindow.configure(bg="#08333E")
            
            image = ImageTk.PhotoImage(Image.open("assets/jarad.png").resize((0x64, 0x64), Image.ANTIALIAS))
            logo = Label(nwindow, image=image, anchor=CENTER, bd=0)
            logo.image = image
            logo.pack(pady=0xA)
            
            Label(nwindow, text="This application is developed by JARAD Company", bg="#08333E", fg="white", font=('Helvetica 11')).pack()
            Button(nwindow, text="Visit Developer's profile", command=dev, bd=0x0, bg="#08333E",fg="yellow", font= ('Helvetica 8 underline')).pack(pady=0x5)
            Button(nwindow, text="Source", command=source, bd=0x0, bg="#08333E", fg="yellow", font= ('Helvetica 8 underline')).pack(pady=0x3)
            
        def clearAllForm(self): pass
            
        def setMenuBar(self):
            # _FILE_
            file_menu = Menu(self.menu, tearoff=0x0)
            file_menu.add_command(label="Save as PDF", command=self.printToPdf)
            file_menu.add_command(label="Exit", command=self.exit)
            
            #__EDIT__
            edit_menu = Menu(self.menu, tearoff=0x0)
            edit_menu.add_command(label="Clear", command=self.clearAllForm)
            
            # __HELP__
            help_menu = Menu(self.menu, tearoff=0x0)
            help_menu.add_command(label="About Developer", command=self.about)
            
            self.menu.add_cascade(label="File", menu=file_menu)
            self.menu.add_cascade(label="Edit", menu=edit_menu)
            self.menu.add_cascade(label="Help", menu=help_menu)
            self.window.config(menu=self.menu)
            
        def exit(self): self.window.destroy()
        
        def printToPdf(self): pass
        
        def _entry(self, frame, name, position):
            entry = Entry(frame, textvariable=name, width=20).grid(row=position['row'], column=position['column'])
            
            return entry.get()
        
        def userForms(self):
            global UserFrame
            
            UserFrame = Frame(self.window)
            UserFrame.configure(width=100, height=600, bg="#08333E")
            
            EmployeeNameLabel = Label(UserFrame, text="Employee Name: ", bd=0x0, bg="#08333E", fg="white").grid(row=0x3)
            EmployeeNameInput = self._entry(frame=UserFrame, name="Employee", position={ "row" : 0x3, "column" :0x1})
            
            
            UserFrame.pack(side=TOP, pady=0xA)
            
        def run(self):
            # Set the window's size 
            self.window.geometry("350x600+50+50")
            # Set icon for the window
            self.window.iconbitmap(self.window, 'assets/app.ico')
            # Set title for the window
            self.window.wm_title(string=self.title)
            self.window.configure(bg="#08333E")
            # Set Menu bar
            self.setMenuBar()
            # Render form
            self.userForms()
            
            print(EmployeeNameInput.get())
            # Execute the window
            self.window.mainloop()
        
if __name__ == "__main__":
    hr = HR().System(version=1.0, application="HR System")
    hr.run()
        