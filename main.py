import random
from tkinter import *

BG = "#ece3dc"
BUTTON_FONT = ("times new roman", 15, "italic")
BUTTON_BG = "#B2533E"
WELCOME_FONT = ("lucida handwriting", 30, "normal")


word_index = 0
welcome_list = ["Welcome", "To  My", "\"Rock, Paper, Scissor Game\""]
welcome_string = ""
user_input = None
computer_input = None
player_score = 0
computer_score = 0


def welcome():
    global word_index, welcome_list, welcome_string
    if word_index < len(welcome_list):
        welcome_string += welcome_list[word_index] + "\n"
        canvas.itemconfig(welcome_font, text=welcome_string)
        word_index += 1
        window.after(800, welcome)
    else:
        window.after_cancel(welcome_animation)
        canvas.config(width=700, height=300)
        canvas.delete(welcome_font)
        player_score_label.grid(row=0, column=0)
        enemy_score_label.grid(row=0, column=2)
        rock_button.grid(row=2, column=0)
        paper_button.grid(row=2, column=1)
        scissor_button.grid(row=2, column=2)


def rock():
    global user_input, computer_input
    user_input = 0
    canvas.itemconfig(user_input_image, image=rock_image)
    computer_input = ai_draw()
    check(user_input, computer_input)


def paper():
    global user_input, computer_input
    user_input = 1
    canvas.itemconfig(user_input_image, image=paper_image)
    computer_input = ai_draw()
    check(user_input, computer_input)


def scissor():
    global user_input, computer_input
    user_input = 2
    canvas.itemconfig(user_input_image, image=scissor_image)
    computer_input = ai_draw()
    check(user_input, computer_input)


def ai_draw():
    ai_input = random.randint(0, 2)
    if ai_input == 0:
        canvas.itemconfig(ai_input_image, image=rock_image)
    elif ai_input == 1:
        canvas.itemconfig(ai_input_image, image=paper_image)
    elif ai_input == 2:
        canvas.itemconfig(ai_input_image, image=scissor_image)
    return ai_input


def check(user, computer):
    global player_score, computer_score
    # rock: 0 paper: 1 scissor: 2
    if user == 0 and computer == 2:
        player_score += 1
        canvas.itemconfig(compare_text, text=">")
    elif user == 2 and computer == 0:
        computer_score += 1
        canvas.itemconfig(compare_text, text="<")
    elif user > computer:
        player_score += 1
        canvas.itemconfig(compare_text, text=">")
    elif computer > user:
        canvas.itemconfig(compare_text, text="<")
        computer_score += 1
    else:
        canvas.itemconfig(compare_text, text="=")
    player_score_label.config(text=f'Your Score: {player_score}')
    enemy_score_label.config(text=f"AI Score: {computer_score}")


window = Tk()
window.title("Rock Paper Scissor")
window.config(padx=50, pady=50, bg=BG)


# labels
player_score_label = Label(text=f'Your Score: {player_score}', fg="#CD5C08", bg=BG, font=("Lucida Console", 18, "bold"))
player_score_label.config(padx=20, pady=5)

enemy_score_label = Label(text=f"AI Score: {computer_score}", fg="#CD5C08", bg=BG, font=("Lucida Console", 18, "bold"))
enemy_score_label.config(padx=20, pady=5)

# main game screen
canvas = Canvas(width=700, height=400, highlightthickness=0, bg=BG)
canvas.grid(row=1, column=0, columnspan=3)
welcome_font = canvas.create_text(350, 150, text="", font=WELCOME_FONT, fill="#C70039")
welcome_animation = window.after(1000, func=welcome)
compare_text = canvas.create_text(350, 150, text="", fill="#E55604", font=("times new roman", 40, "bold"))


rock_image = PhotoImage(file="assets/images/rock.png").subsample(2, 2)
paper_image = PhotoImage(file="assets/images/paper.png").subsample(2, 2)
scissor_image = PhotoImage(file="assets/images/scissors.png").subsample(2, 2)

user_input_image = canvas.create_image(125, 125, image=None)
ai_input_image = canvas.create_image(575, 125, image=None)

# buttons
rock_button = Button(text="Rock", font=BUTTON_FONT, bg=BUTTON_BG, command=rock)
rock_button.config(padx=20, pady=5)

paper_button = Button(text="Paper", font=BUTTON_FONT, bg=BUTTON_BG, command=paper)
paper_button.config(padx=20, pady=5)

scissor_button = Button(text="Scissor", font=BUTTON_FONT, bg=BUTTON_BG, command=scissor)
scissor_button.config(padx=20, pady=5)

window.mainloop()
