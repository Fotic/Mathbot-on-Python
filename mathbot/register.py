from tkinter import *
import requests

BG_COLOR = "#0091FE"
BUTTON_COLOR = "#000"
BUTTON_BG_COLOR = "#FFF"
LABEL_COLOR = "#fff"
LABEL_BG_COLOR = "#fff"
TEXT_COLOR = "#000"
TEXT_BG_COLOR = "#fff"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

class MathBot:

    def register_screen(self):
        # self.login_screen.destroy()

        self.register_screen = self.create_windows("MathBot Register", 550, 400)

        # label
        label = Label(self.register_screen, text='Εγγραφή', bg=BG_COLOR, fg=LABEL_COLOR, font=FONT)
        label.place(anchor=CENTER, relx=.5, rely=0.05)

        # divider
        line = Label(self.register_screen, width=450, bg=BUTTON_BG_COLOR)
        line.place(relwidth=1, rely=0.1, relheight=0.012)

        # label
        label = Label(self.register_screen, text='Όνομα', bg=BG_COLOR, fg=LABEL_COLOR, font=FONT)
        label.place(anchor=CENTER, relx=.15, rely=.2)

        # text field
        self.f_name = Entry(self.register_screen, width=25, bg=TEXT_BG_COLOR, fg=TEXT_COLOR, font=FONT)
        self.f_name.place(anchor=CENTER, relx=.55, rely=.2)

        # label
        label = Label(self.register_screen, text='Επώνυμο', bg=BG_COLOR, fg=LABEL_COLOR, font=FONT)
        label.place(anchor=CENTER, relx=.15, rely=.3)

        # text field
        self.l_name = Entry(self.register_screen, width=25, bg=TEXT_BG_COLOR, fg=TEXT_COLOR, font=FONT)
        self.l_name.place(anchor=CENTER, relx=.55, rely=.3)

        # label
        label = Label(self.register_screen, text='Όνομα Χρήστη', bg=BG_COLOR, fg=LABEL_COLOR, font=FONT)
        label.place(anchor=CENTER, relx=.15, rely=.4)

        # text field
        self.user_name = Entry(self.register_screen, width=25, bg=TEXT_BG_COLOR, fg=TEXT_COLOR, font=FONT)
        self.user_name.place(anchor=CENTER, relx=.55, rely=.4)

        # label
        label = Label(self.register_screen, text='Κωδικός Χρήστη', bg=BG_COLOR, fg=LABEL_COLOR, font=FONT)
        label.place(anchor=CENTER, relx=.15, rely=.5)

        # text field
        self.user_password = Entry(self.register_screen, show="*", width=25, bg=TEXT_BG_COLOR, fg=TEXT_COLOR, font=FONT)
        self.user_password.place(anchor=CENTER, relx=.55, rely=.5)

        # label
        label = Label(self.register_screen, text='Επαλ. Κωδικού', bg=BG_COLOR, fg=LABEL_COLOR, font=FONT)
        label.place(anchor=CENTER, relx=.15, rely=.6)

        # text field
        self.password_valid = Entry(self.register_screen, show="*", width=25, bg=TEXT_BG_COLOR, fg=TEXT_COLOR, font=FONT)
        self.password_valid.place(anchor=CENTER, relx=.55, rely=.6)

        # register button
        register_button = Button(self.register_screen, text="Εγγραφή", command=self._register_click, bg=BUTTON_BG_COLOR, fg=BUTTON_COLOR, font=FONT_BOLD)
        register_button.place(anchor=CENTER, relx=.5, rely=.7)

        self.register_screen.mainloop()

    def _register_click(self):
        f_name = self.f_name.get()
        l_name = self.l_name.get()
        user_name = self.user_name.get()
        user_password = self.user_password.get()
        password_valid = self.password_valid.get()

        if len(f_name) == 0:
            self.error_message("Σφάλμα Σύνδεσης", 'Παρακαλώ εισάγεται Όνομα!')
            return
        if len(l_name) == 0:
            self.error_message("Σφάλμα Σύνδεσης", 'Παρακαλώ εισάγεται Επώνυμο!')
            return
        if len(user_name) == 0:
            self.error_message("Σφάλμα Σύνδεσης", 'Παρακαλώ εισάγεται Όνομα Χρήστη!')
            return
        if len(user_password) == 0:
            self.error_message("Σφάλμα Σύνδεσης", 'Παρακαλώ εισάγεται Κωδικό Χρήστη!')
            return
        if len(password_valid) == 0:
            self.error_message("Σφάλμα Σύνδεσης", 'Παρακαλώ εισάγεται Κωδικό Επάλ.!')
            return

        if user_password != password_valid:
            self.error_message("Σφάλμα Εγγραφής", 'Οι κωδικοί δεν αντιστοιχούν!')
            return

        data = "?type=register&f_name=" + f_name + "&l_name=" + l_name + "&user_name=" + user_name + "&user_password=" + user_password
        result = requests.request("POST",self.get_url() + data)
        # print(result.text)
        if result.text == 'register_ok':
            self.register_screen.destroy()
            # app = MathBot()
            # app.login_screen()
        else:
            self.error_message("Σφάλμα Εγγραφής", 'Ο χρήστης υπάρχει ήδη!')
            return


