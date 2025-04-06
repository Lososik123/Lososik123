from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import shuffle    
class Question:

    def __init__(self, question, right_answer, 
                wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions = [
    Question('шаурма?', 'Да', 'Нет', 'Гы)', 'Пэльмэни'),
    Question('Куда ходят школьники?','В алгоритмику', 'В рай', 'В садик', 'В ад'),
    Question('Любишь пельмени?)','Конечно!', 'предпочту шавуху', 'Нит', 'Я вообще Сталин '),
    Question('Самое тупое млекопитающие?','Мой кент', 'Это я', 'Свинки', 'Птички'),
]
question_number = -1
app = QApplication([])
# Создаем панель вопроса
btn_OK = QPushButton('Ответить')
lb_Question = QLabel(questions[question_number].question)


RadioGroupBox = QGroupBox("Варианты ответов")


rbtn_1 = QRadioButton(questions[question_number].right_answer)
rbtn_2 = QRadioButton(questions[question_number].wrong1)
rbtn_3 = QRadioButton(questions[question_number].wrong2)
rbtn_4 = QRadioButton(questions[question_number].wrong3)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
shuffle(answers)

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # два ответа во второй столбец
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)


RadioGroupBox.setLayout(layout_ans1)
# Создаем панель результата
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') # здесь размещается надпись "правильно" или "неправильно"
lb_Correct = QLabel(questions[question_number].right_answer) # здесь будет написан текст правильного ответа
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)


# Размещаем все виджеты в окне:
layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
# Размещаем в одной строке обе панели, одна из них будет скрываться, другая показываться:
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide()

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)


# Теперь созданные строки разместим друг под другой:
layout_card = QVBoxLayout()


layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым
AnsGroupBox.hide()

def check_answer():
    if answers[0].isChecked():
        return True
    return False

def next_question():
    global question_number
    question_number = (question_number + 1) % len(answers)
    lb_Question.setText(questions[question_number].question)
    shuffle(answers)
    answers[0].setText(questions[question_number].right_answer)
    answers[1].setText(questions[question_number].wrong1)
    answers[2].setText(questions[question_number].wrong2)
    answers[3].setText(questions[question_number].wrong3)


def  show_answer():
    if btn_OK.text() == "Ответить":
        btn_OK.setText("Следующий вопрос")
        RadioGroupBox.hide()
        AnsGroupBox.show()
        if check_answer():
            lb_Result.setText('Вы ответили правильно!')
        else:
            lb_Result.setText("Вы ответили неверно!")
        lb_Correct.setText(f"Правильный ответ {answers[0].text()}")
    else:
        btn_OK.setText("Ответить")
        RadioGroupBox.show()
        AnsGroupBox.hide()
        RadioGroup.setExclusive(False)
        rbtn_1.setChecked(False)
        rbtn_2.setChecked(False)
        rbtn_3.setChecked(False)
        rbtn_4.setChecked(False)
        next_question()
btn_OK.clicked.connect(show_answer)
next_question()
window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')
window.resize(400,200)
window.show()
app.exec()