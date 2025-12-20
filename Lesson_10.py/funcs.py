import data
import random

correct_answers_count = 0
quest_index = 0
quests_data = data.questions
random.shuffle(quests_data)

def generate_quest(QUEST, buttons, info):
    global quest_index
    
    if quest_index < len(quests_data):
        QUEST.config(text=quests_data[quest_index]["quest"])
        answers = list(quests_data[quest_index]["answers"])
        random.shuffle(answers)
        for i in range(len(buttons)):
            buttons[i].config(text=answers[i], state="normal")
    else:
        QUEST.config(text=f"Конец! {correct_answers_count} из {len(quests_data)}")
        for btn in buttons:
            btn.config(state="disabled")
def choice(button, QUEST, buttons, info):
    global quest_index
    global correct_answers_count
    if button["text"] == quests_data[quest_index]["right"]:
        correct_answers_count += 1 
    quest_index += 1
    generate_quest(QUEST, buttons, info)