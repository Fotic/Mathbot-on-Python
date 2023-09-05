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

    def login_screen(self):
        self.login_screen = self.create_windows("MathBot Login", 550, 250)

        # label
        label = Label(self.login_screen, text='MathBot', bg=BG_COLOR, fg=LABEL_COLOR, font=FONT)
        label.place(anchor=CENTER, relx=.5, rely=.08)

        # divider
        line = Label(self.login_screen, width=450, bg=BUTTON_BG_COLOR)
        line.place(relwidth=1, rely=0.16, relheight=0.012)

        # label
        label = Label(self.login_screen, text='Όνομα Χρήστη', bg=BG_COLOR, fg=LABEL_COLOR, font=FONT)
        label.place(anchor=CENTER, relx=.15, rely=.3)

        # text field
        self.username = Entry(self.login_screen, width=25, bg=TEXT_BG_COLOR, fg=TEXT_COLOR, font=FONT)
        self.username.place(anchor=CENTER, relx=.55, rely=.3)
        self.username.bind("<Return>", self._login_click)

        # label
        label = Label(self.login_screen, text='Κωδικός Χρήστη', bg=BG_COLOR, fg=LABEL_COLOR, font=FONT)
        label.place(anchor=CENTER, relx=.15, rely=.45)

        # text field
        self.password = Entry(self.login_screen, show="*", width=25, bg=TEXT_BG_COLOR, fg=TEXT_COLOR, font=FONT)
        self.password.place(anchor=CENTER, relx=.55, rely=.45)
        self.password.bind("<Return>", self._login_click) #bind enter button

        # login button
        login_button = Button(self.login_screen, text="Σύνδεση", command=lambda: self._login_click(None), bg=BUTTON_BG_COLOR, fg=BUTTON_COLOR, font=FONT_BOLD)
        login_button.place(anchor=CENTER, relx=.5, rely=.65)

        # info button
        info_button = Button(self.login_screen, text="Πληροφορίες", command=self._info_screen_click, bg=BUTTON_BG_COLOR, fg=BUTTON_COLOR, font=FONT_BOLD)
        info_button.place(anchor=CENTER, relx=.85, rely=.8)

        register_button = Button(self.login_screen, text="Εγγραφή", command=self.register_screen, bg=BUTTON_BG_COLOR, fg=BUTTON_COLOR, font=FONT_BOLD)
        register_button.place(anchor=CENTER, relx=.15, rely=.8)

        self.login_screen.mainloop()

    def _login_click(self,event):
        user = self.username.get()
        user_pass = self.password.get()

        if len(user) == 0:
            self.error_message("Σφάλμα Σύνδεσης", 'Παρακαλώ εισάγεται Όνομα Χρήστη!')
            return
        if len(user_pass) == 0:
            self.error_message("Σφάλμα Σύνδεσης", 'Παρακαλώ εισάγεται Κωδικό Σύνδεσης!')
            return

        data = "?type=login&user_name=" + user + "&user_password=" + user_pass
        result = requests.request("POST", self.get_url() + data)
        # print(result.text)

        if result.text != 'login_error':
            self.db_f_name = result.text
            self.db_user_name = self.username.get()
            self.login_screen.destroy()
            self.mathbot_screen()
        else:
            self.error_message("Σφάλμα Σύνδεσης",'Ο χρήστης δεν βρέθηκε!')
            return

    def _info_screen_click(self):
        info_screen = self.create_windows("Info", 600, 400)

        label = Label(info_screen, text="""
        Σχολή:
        Διεθνές Πανεπιστήμιο Ελλάδος\n
        Πρόγραμμα:
        MPhil Προηγμένες Τεχνολογίες Πληροφορικής και Υπολογιστών\n
        Μάθημα:
        Προχωρημένος Προγραμματισμός και 
        Ανάπτυξη Εμπλουτισμένων Εφαρμογών Διαδικτύου\n
        Διδάσκων:
        Ελευθέριος Μωυσιάδης\n
        Μεταπτυχιακός Φοιτητής:
        Παπαρούνας Φώτιος
        ΑΜ: 117
        """, bg=BG_COLOR, fg=LABEL_COLOR, font=FONT)
        label.place(anchor=CENTER, relx=.5, rely=.5)

        info_screen.mainloop()


