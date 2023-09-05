from tkinter import *
import requests
import random

import login,register,statistic

BG_COLOR = "#0091FE"
BUTTON_COLOR = "#000"
BUTTON_BG_COLOR = "#FFF"
LABEL_COLOR = "#fff"
LABEL_BG_COLOR = "#fff"
TEXT_COLOR = "#000"
TEXT_BG_COLOR = "#fff"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"
EQUATION, NUM1, NUM2 = '', 0, 0

class MathBot(login.MathBot, register.MathBot, statistic.MathBot):

    def get_url(self):
        return "http://test.gr/query.php"

    def create_windows(self, name, width, height):
        self.window = Tk()
        self.window.title(name)
        self.window.resizable(width=False, height=False)
        self.window.configure(width=width, height=height, bg=BG_COLOR)
        return self.window

    def error_message(self, window_name, message):
        window = self.create_windows(window_name, 400, 100)
        l0 = Label(window, text=message, bg=BG_COLOR, fg=LABEL_COLOR, font=FONT)
        l0.place(anchor=CENTER, relx=.5, rely=.4)
        window.mainloop()

    def mathbot_screen(self):
        self.mathbot = self.create_windows("MathBot", 470, 550)

        # self.db_f_name = 'Φωτης'
        # self.db_user_name = 'fotis'

        # label
        label = Label(self.mathbot, bg=BG_COLOR, fg=LABEL_COLOR,
                           text=f"Γεια σου {self.db_f_name}", font=FONT_BOLD, pady=10)
        label.place(relwidth=1)

        score_button = Button(self.mathbot, text="Score", font=FONT_BOLD, width=20, bg=BUTTON_BG_COLOR,
                             command=self.highscore_screen_click)
        score_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

        # divider
        line = Label(self.mathbot, width=450, bg=BUTTON_BG_COLOR)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # text widget
        self.chatbox = Text(self.mathbot, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5)
        self.chatbox.place(relheight=0.745, relwidth=0.97, rely=0.08)
        self.chatbox.configure(cursor="arrow", state=DISABLED)

        # scroll bar
        scrollbar = Scrollbar(self.mathbot, command=self.chatbox.yview)
        scrollbar.place(relheight=0.74, rely=0.083, relx=0.963)
        scrollbar.configure(command=self.chatbox.yview)
        self.chatbox.configure(yscrollcommand=scrollbar.set)

        # bottom label
        bottom_label = Label(self.mathbot, bg=BG_COLOR, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        # message entry box
        self.msg_entry = Entry(bottom_label, bg=TEXT_BG_COLOR, fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._enter_click) #bind enter button

        # send button
        send_button = Button(bottom_label, text="Enter", font=FONT_BOLD, width=20, bg=BUTTON_BG_COLOR,
                             command=lambda: self._enter_click(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

        msg2 = f"BOT: Γεια σου {self.db_f_name},\nΤι πράξη θέλετε να κάνετε πρόσθεση, αφαίρεση, πολλαπλασισμό ή διαίρεση;\n\n"
        self.chatbox.configure(state=NORMAL, fg=LABEL_COLOR)
        self.chatbox.insert(END, msg2)
        self.chatbox.configure(state=DISABLED)

        self.mathbot.mainloop()

    def _enter_click(self, event):
        global EQUATION, NUM1, NUM2
        msg = self.msg_entry.get()

        if not msg:
            return

        self.msg_entry.delete(0, END)
        msg1 = f"{self.db_f_name}: {msg}\n\n"
        self._show_message(msg1)

        if self._is_number(msg):
            if EQUATION == 'προσθεση':
                msg2 = "ΒΟΤ: Σωστά\n\n" if (NUM1 + NUM2) == float(msg) else "ΒΟΤ: Λάθος\n\n"
                self._show_message(msg2)

                data = f"?type=set_highscore&user_name={self.db_user_name}&equation=prosthesi&new_total={1 if (NUM1 + NUM2) == float(msg) else 0}"
                requests.request("POST", self.get_url() + data)

                NUM1 = random.randint(1, 100)
                NUM2 = random.randint(1, 100)
                msg2 = "ΒΟΤ: Η πράξη: " + str(NUM1) + " + " + str(NUM2) + " τι αποτέλεσμα δίνει;\n\n"
                self._show_message(msg2)
            elif EQUATION == 'αφαιρεση':
                msg2 = "ΒΟΤ: Σωστά\n\n" if (NUM1 - NUM2) == float(msg) else "ΒΟΤ: Λάθος\n\n"
                self._show_message(msg2)

                data = f"?type=set_highscore&user_name={self.db_user_name}&equation=afairesi&new_total={1 if (NUM1 - NUM2) == float(msg) else 0}"
                requests.request("POST", self.get_url() + data)

                NUM1 = random.randint(1, 100)
                NUM2 = random.randint(1, 100)
                msg2 = "ΒΟΤ: Η πράξη: " + str(NUM1) + " - " + str(NUM2) + " τι αποτέλεσμα δίνει;\n\n"
                self._show_message(msg2)
            elif EQUATION == 'πολλαπλασισμό':
                msg2 = "ΒΟΤ: Σωστά\n\n" if (NUM1 * NUM2) == float(msg) else "ΒΟΤ: Λάθος\n\n"
                self._show_message(msg2)

                data = f"?type=set_highscore&user_name={self.db_user_name}&equation=pollaplasiasmo&new_total={1 if (NUM1 * NUM2) == float(msg) else 0}"
                requests.request("POST", self.get_url() + data)

                NUM1 = random.randint(1, 100)
                NUM2 = random.randint(1, 100)
                msg2 = "ΒΟΤ: Η πράξη: " + str(NUM1) + " * " + str(NUM2) + " τι αποτέλεσμα δίνει;\n\n"
                self._show_message(msg2)
            elif EQUATION == 'διαιρεση':
                msg2 = "ΒΟΤ: Σωστά\n\n" if ( round(NUM1 / NUM2,2) ) == float(msg) else "ΒΟΤ: Λάθος\n\n"
                self._show_message(msg2)

                data = f"?type=set_highscore&user_name={self.db_user_name}&equation=diairesi&new_total={1 if ( round(NUM1 / NUM2,2) ) == float(msg) else 0}"
                requests.request("POST", self.get_url() + data)

                NUM1 = random.randint(1, 100)
                NUM2 = random.randint(1, 100)
                msg2 = "ΒΟΤ: Η πράξη: " + str(NUM1) + " / " + str(NUM2) + " τι αποτέλεσμα δίνει;\n\n"
                self._show_message(msg2)
            else:
                msg2 = "ΒΟΤ: Επιλέξτε πράξη πρώτα παρακαλώ!\n\n"
                self._show_message(msg2)
        else:
            NUM1 = random.randint(1, 100)
            NUM2 = random.randint(1, 100)
            if any(value in ['προσθεση','πρόσθεση','prosthesi','prosthesh','+'] for value in msg.lower().split(' ')):
                EQUATION = 'προσθεση'
                msg2 = "ΒΟΤ: Η πράξη: " + str(NUM1) + " + " + str(NUM2) + " τι αποτέλεσμα δίνει;\n\n"
                self._show_message(msg2)
            elif any(value in ['αφαιρεση','αφαίρεση','aferesi','aferesh','afairesi','afairesh','-'] for value in msg.lower().split(' ')):
                EQUATION = 'αφαιρεση'
                msg2 = "ΒΟΤ: Η πράξη: " + str(NUM1) + " - " + str(NUM2) + " τι αποτέλεσμα δίνει;\n\n"
                self._show_message(msg2)
            elif any(value in ['πολλαπλασιασμο','πολλαπλασιασμό','pollaplasiasmo','polaplasiasmo','*'] for value in msg.lower().split(' ')):
                EQUATION = 'πολλαπλασισμό'
                msg2 = "ΒΟΤ: Η πράξη: " + str(NUM1) + " * " + str(NUM2) + " τι αποτέλεσμα δίνει;\n\n"
                self._show_message(msg2)
            elif any(value in ['διαιρεση','διαίρεση','diairesi','diairesh','dieresi','dieresh','/'] for value in msg.lower().split(' ')):
                EQUATION = 'διαιρεση'
                msg2 = "ΒΟΤ: Η πράξη: " + str(NUM1) + " / " + str(NUM2) + " τι αποτέλεσμα δίνει;\n\n"
                self._show_message(msg2)
            else:
                msg2 = "ΒΟΤ: Δεν κατάλαβα αναδιατυπώστε παρακαλώ!\n\n"
                self._show_message(msg2)

        self.chatbox.see(END)

    def _is_number(self, string):
        try:
            float(string)
            return True
        except ValueError:
            return False

    def _show_message(self, msg):
        self.chatbox.configure(state=NORMAL)
        self.chatbox.insert(END, msg)
        self.chatbox.configure(state=DISABLED)

if __name__ == "__main__":
    app = MathBot()
    app.login_screen()
    # app.mathbot_screen()