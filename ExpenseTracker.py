import customtkinter as ctk
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")
class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Expense Tracker")    
        self.geometry("1920x1080")
        self.f1()
        self.wlcm()
        self.f2()
    def f1(self):
        self.frame = ctk.CTkFrame(master=self, width=400, height=400, border_color="White", fg_color="cyan")
        self.frame.pack(padx=20, pady=20)
    def wlcm(self):
        label = ctk.CTkLabel(master=self.frame, text="Welcome!",text_color="blue", fg_color="transparent")
        label.pack(padx=20, pady=20)
    def f2(self):
        self.frame = ctk.CTkFrame(master=self, width= 400, height= 400, fg_color="white")
        self.frame.pack(padx=20, pady=20)
if __name__ == "__main__":
    app = App()
    app.mainloop()