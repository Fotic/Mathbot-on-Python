from tkinter import *
import requests

BG_COLOR = "#0091FE"
BUTTON_COLOR = "#000"
BUTTON_BG_COLOR = "#FFF"
LABEL_COLOR = "#fff"
LABEL_BG_COLOR = "#fff"
TEXT_COLOR = "#fff"
TEXT_BG_COLOR = "#fff"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

class MathBot:

    def highscore_screen_click(self):
        highscore_screen = self.create_windows("Ηighscore", 470, 400)

        data = f"?type=get_highscore&user_name={self.db_user_name}"
        result = requests.request("POST", self.get_url() + data)
        # print(result.text)
        result = (result.text).split('-')

        # head label
        label = Label(highscore_screen, bg=BG_COLOR, fg=TEXT_COLOR,
                           text=f"Στατιστικά", font=FONT_BOLD, pady=10)
        label.place(relwidth=1)

        # divider
        line = Label(highscore_screen, width=450, bg=BUTTON_BG_COLOR)
        line.place(relwidth=1, rely=0.1, relheight=0.012)

        info = f"""Απαντήσεις:\n\nΠρόσθεση:\nΑφαίρεση:\nΠολλαπλασισμό:\nΔιαίρεση:"""
        label = Label(highscore_screen, bg=BG_COLOR, fg=TEXT_COLOR,
                      text=info, font=FONT, pady=5)
        label.place(relx=.15,rely=.14)

        info = f"{result[0]} από {result[1]}\n\n{result[2]} από {result[3]}\n{result[4]} από {result[5]}\n{result[6]} από {result[7]}\n{result[8]} από {result[9]}"
        label = Label(highscore_screen, bg=BG_COLOR, fg=TEXT_COLOR,
                      text=info, font=FONT, pady=5)
        label.place(relx=.50,rely=.14)

        # divider
        line = Label(highscore_screen, width=450, bg=BG_COLOR)
        line.place(relwidth=1, rely=0.5, relheight=0.012)

        # top 10 label
        label = Label(highscore_screen, bg=BG_COLOR, fg=TEXT_COLOR,
                      text=f"TOP 10", font=FONT_BOLD, pady=5)
        label.place(relwidth=1,rely=.51)

        # top 10 buttons
        top_ten_button = Button(highscore_screen, text="Πρόσθεση", command=lambda: self._top_ten_click("Πρόσθεση",'prosthesi'),bg=BUTTON_BG_COLOR, fg=BUTTON_COLOR, font=FONT_BOLD)
        top_ten_button.place(anchor=CENTER, relwidth=.5, relx=.5, rely=.65)

        top_ten_button = Button(highscore_screen, text="Αφαίρεση", command=lambda: self._top_ten_click("Αφαίρεση",'afairesi'),bg=BUTTON_BG_COLOR, fg=BUTTON_COLOR, font=FONT_BOLD)
        top_ten_button.place(anchor=CENTER, relwidth=.5, relx=.5, rely=.75)

        top_ten_button = Button(highscore_screen, text="Πολλαπλασιασμό", command=lambda: self._top_ten_click("Πολλαπλασιασμό",'pollaplasiasmo'),bg=BUTTON_BG_COLOR, fg=BUTTON_COLOR, font=FONT_BOLD)
        top_ten_button.place(anchor=CENTER, relwidth=.5, relx=.5,rely=.85)

        top_ten_button = Button(highscore_screen, text="Διαίρεση", command=lambda: self._top_ten_click("Διαίρεση",'diairesi'), bg=BUTTON_BG_COLOR, fg=BUTTON_COLOR, font=FONT_BOLD)
        top_ten_button.place(anchor=CENTER, relwidth=.5, relx=.5, rely=.95)

        highscore_screen.mainloop()

    def _top_ten_click(self, equation_name, equation_type):
        top_ten_screen = self.create_windows(f"{equation_name} TOP 10", 470, 300)

        data = f"?type=get_top_ten&equation={equation_type}"
        result = requests.request("POST", self.get_url() + data)
        # print(result.text)
        # head label
        label = Label(top_ten_screen, bg=BG_COLOR, fg=TEXT_COLOR,
                      text=f"{equation_name} TOP 10", font=FONT_BOLD, pady=10)
        label.place(relwidth=1)

        # divider
        line = Label(top_ten_screen, width=450, bg=BUTTON_BG_COLOR)
        line.place(relwidth=1, rely=0.15, relheight=0.012)

        label = Label(top_ten_screen, bg=BG_COLOR, fg=TEXT_COLOR,
                      text=f"Χρήστης : Score", font=FONT_BOLD)
        label.place(relwidth=1, rely=.2)

        # user : score
        label = Label(top_ten_screen, bg=BG_COLOR, fg=TEXT_COLOR,
                      text=result.text, font=FONT_BOLD, pady=5)
        label.place(relwidth=1, rely=.3)

        top_ten_screen.mainloop()
