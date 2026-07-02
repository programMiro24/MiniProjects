import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.geometry("450x320")
root.title("Викторина България")

questions = [
    {
        "question": "Кой град е известен \n с името Малката Виена?",
        "answers": ["София", "Варна", "Бургас", "Русе"],
        "correct": 4
    },
    {
        "question": "В коя област протича река Велека?",
        "answers": ["Дунавска равнина", "Страндажнско-Тракийска", "Рило-Родопоска", "Крайщенско-Средногорска"],
        "correct": 2
    },
    {
        "question": "В коя област е включена\n планината Люлин?",
        "answers": ["Старопланинска", "Рило-Родопска", "Крайщенско-Средногорска", "Странджанско-Тракийска"],
        "correct": 3
    },
]

current_question = 0
score = 0

def check_answer(index):
    global score, current_question
    if questions[current_question]['correct'] == index:
        score += 1
    if current_question == len(questions) - 1:
        message_string = "Трябва да поучиш малко."
        if score >= 0.80 * len(questions):
            message_string = "Ти си мастър по география."
        messagebox.showinfo("Край на викторината", message=message_string)
        root.destroy()
    else:
        current_question += 1
        update_question()


def update_question():
    question.set(questions[current_question]['question'])
    answer1.set(questions[current_question]['answers'][0])
    answer2.set(questions[current_question]['answers'][1])
    answer3.set(questions[current_question]['answers'][2])
    answer4.set(questions[current_question]['answers'][3])
    for button in buttons:
        button.config(state=tk.NORMAL)
    result.set(f"Резултат: {score} от {len(questions)}")

def add_joker():
    index = [0, 1, 2, 3]
    correct_answer = questions[current_question]['correct']-1
    index.remove(correct_answer)
    ans1 = random.choice(index)
    index.remove(ans1)
    ans2 = random.choice(index)
    buttons[ans1].config(state=tk.DISABLED)
    buttons[ans2].config(state=tk.DISABLED)
    joker.config(state = tk.DISABLED)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

tk.Label(root, text="България", font=("Arial", 15, "bold"), fg="darkslategray").grid(row=0, column=0, columnspan=2,
                                                                                    sticky="ew", pady=10)
question = tk.StringVar()
question.set(questions[0]['question'])
tk.Label(root, textvariable=question, font=("Arial", 15, "bold")).grid(row=1, column=0, columnspan=2,
                                                                       sticky="ew", pady=10)
answer1 = tk.StringVar()
answer1.set(questions[0]["answers"][0])
button1 = (tk.Button(root, textvariable=answer1, command=lambda: check_answer(1),
          font=("Helvetica", 12)))
button1.grid(row=2, column=0, pady=10, padx=10)

answer2 = tk.StringVar()
answer2.set(questions[0]["answers"][1])
button2 = tk.Button(root, textvariable=answer2, command=lambda: check_answer(2),
          font=("Helvetica", 12))
button2.grid(row=2, column=1, pady=10)

answer3 = tk.StringVar()
answer3.set(questions[0]["answers"][2])
button3 = tk.Button(root, textvariable=answer3, command=lambda: check_answer(3),
          font=("Helvetica", 12))
button3.grid(row=3, column=0, pady=10, padx=10)

answer4 = tk.StringVar()
answer4.set(questions[0]["answers"][3])
button4 = tk.Button(root, textvariable=answer4, command=lambda: check_answer(4),
          font=("Helvetica", 12))
button4.grid(row=3, column=1, pady=10)

buttons = [button1, button2, button3, button4]

joker = tk.Button(root, text="Жокер 50/50", command=add_joker, state=tk.NORMAL)
joker.grid(row=4,column=0, pady=5, columnspan=2)


result = tk.StringVar()
result.set(f"Резултат: 0 от {len(questions)}")
tk.Label(root, textvariable=result, font=("Times New Roman", 15)).grid(row=5,column=0,
                                                                    sticky="ew", pady=10, columnspan=2)



root.mainloop()
