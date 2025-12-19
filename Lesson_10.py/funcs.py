import data
import random
points = 0
correct_answers_count = 0

random_quests_data = list(data.questions)
random.shuffle(random_quests_data)

quest_index = 0

def generate_quest(QUEST, buttons, info):
    global quest_index
    global correct_answers_count
    
    if quest_index < len(random_quests_data):
        current_quest_data = random_quests_data[quest_index]
        
        QUEST.config(text=current_quest_data["quest"])
        
        shuffled_answers = list(current_quest_data["answers"])
        random.shuffle(shuffled_answers)

        for i in range(len(buttons)):
            buttons[i].config(text=shuffled_answers[i], state="normal")
            
        info.config(text="")
    else:
        QUEST.config(text=f"Викторина окончена\nПравильных ответов: {correct_answers_count} из {len(random_quests_data)}")
        for btn in buttons:
            btn.config(state="disabled")
        info.config(text="")

def choice(button, QUEST, buttons, info):
    global quest_index
    global correct_answers_count
    
    current_quest_data = shuffled_quests_data[quest_index]

    if button["text"] == current_quest_data["right"]:
        correct_answers_count += 1
        info.config(text="Верно!")
    else:
        info.config(text="Неверно!")
        
    quest_index += 1
    generate_quest(QUEST, buttons, info)
