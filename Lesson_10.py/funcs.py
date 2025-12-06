import data
points = 0
quest_index = 0
quests_data = data.questions

def generate_quest(QUEST, buttons):
    if quest_index < len(quests_data):
        quest = quests_data[quest_index]["quest"]
        QUEST.config(text=quest)
        for i in range(len(buttons)):
            buttons[i].config(text=quests_data[quest_index]["answers"][i])
    else:
        QUEST.config(text="Викторина закончена")
        for btn in buttons:
            btn.config(state="disabled")
def choice(button, QUEST, buttons, info):
    global quest_index
    if button["text"] == quests_data[quest_index]["right"]:
        quest_index += 1 
        info.config(text="")
        generate_quest(QUEST, buttons)
    else:
        info.config(text="Неверно")

score = 0  # создаем переменную для счетчика очков 
 
# ... 
 
if board[y][x] == "+":  # если по координате головы змейки находится яблоко 
    board[y][x] = "."   # убираем яблоко со старого места 
    y = randint(0, n - 1) 
    x = randint(0, n - 1) 
    board[y][x] = "+"   # размещаем новое яблоко на новом случайном месте 
    score += 1  # увеличиваем счетчик очков на 1 