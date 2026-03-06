#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import ( QApplication, QWidget, QLabel,
                                QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox, QGroupBox,
                                QPushButton, QButtonGroup)
from random import *
class Question():
    def __init__(self, question, right, wrong1, wrong2, wrong3):
        self.question = question
        self.right = right
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
    
app = QApplication([])
okno = QWidget()
okno.resize(400, 250)
okno.setWindowTitle('Memory Card')
text1 = QLabel('Какой национальности не существует')
#создание 1 группы
RadioGroupBox = QGroupBox('Варианты ответов')
answer1 = QRadioButton('Энцы')
answer2 = QRadioButton('Чулымцы')
answer3 = QRadioButton('Смурфы')
answer4 = QRadioButton('Алеуты')
Radio_group = QButtonGroup()
Radio_group.addButton(answer1)
Radio_group.addButton(answer2)
Radio_group.addButton(answer3)
Radio_group.addButton(answer4)
layout1 = QVBoxLayout()
layout2 = QVBoxLayout()
layout1.addWidget(answer1)
layout1.addWidget(answer2)
layout2.addWidget(answer3)
layout2.addWidget(answer4)
layout3 = QHBoxLayout()
layout3.addLayout(layout1)
layout3.addLayout(layout2)
RadioGroupBox.setLayout(layout3)
#создание 2 группы
RadioGroupBox2 = QGroupBox('Результат теста')
text2 = QLabel('Правильно/неправильно')
text3 = QLabel('Правильный ответ')
layout4 = QVBoxLayout()
layout4.addWidget(text2, alignment = Qt.AlignLeft| Qt.AlignTop)
layout4.addWidget(text3, alignment = Qt.AlignHCenter, stretch = 2)
RadioGroupBox2.setLayout(layout4)
otvet = QPushButton('ответить')
main_layout1 = QHBoxLayout()
main_layout2 = QHBoxLayout()
main_layout3 = QHBoxLayout()
main_layout1.addWidget(text1, alignment = Qt.AlignHCenter)
main_layout2.addWidget(RadioGroupBox)
main_layout2.addWidget(RadioGroupBox2)
main_layout3.addStretch(1)
main_layout3.addWidget(otvet, stretch = 2)
main_layout3.addStretch(1)
main_layout = QVBoxLayout()
main_layout.addLayout(main_layout1, stretch = 2)
main_layout.addLayout(main_layout2, stretch = 8)
main_layout.addLayout(main_layout3)
main_layout.setSpacing(20)
okno.setLayout(main_layout)
RadioGroupBox2.hide()
def start_test():
    if otvet.text() == 'ответить':
        show_result()
    else:
        show_question()
def show_result():
    RadioGroupBox.hide()
    RadioGroupBox2.show()
    otvet.setText('Следующий вопрос')
def show_question():
    RadioGroupBox2.hide()
    RadioGroupBox.show()
    otvet.setText('ответить')
    Radio_group.setExclusive(False)
    answer1.setChecked(False)
    answer2.setChecked(False)
    answer3.setChecked(False)
    answer4.setChecked(False)
    Radio_group.setExclusive(True)
answers = [answer1, answer2, answer3, answer4]
def ask(q):
    shuffle(answers)
    answers[0].setText(q.right)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    text1.setText(q.question)
    text3.setText(q.right)
    show_question()
def check_answer():
    if answers[0].isChecked():
        show_correct('правильно')
        okno.total_score += 1
    else:
        show_correct('неправильно')
    print('Статистика:')
    print("всего вопросов:", okno.total_question)
    print('правильных ответов:', okno.total_score)
    print('Рейтинг', (okno.total_score / okno.total_question) * 100, '%\n')
    question_list.remove(question_list[okno.cur_question])
def show_correct(result):
    text2.setText(result)
    show_result()
def click_OK():
    if otvet.text() == 'ответить':
        check_answer()
    else:
        if len(question_list) > 0:
            next_question()
okno.total_question = 0
okno.total_score = 0
def next_question():
    okno.cur_question = randint(0, len(question_list) -1)
    okno.total_question += 1
    print('Статистика:')
    print("всего вопросов:", okno.total_question)
    print('правильных ответов:', okno.total_score,'\n')
    ask(question_list[okno.cur_question])
question_list = list()
q1 = Question('Государственный язык Бразилии', 'Португальский', 'Русский', 'Итальянский', 'Английский')
question_list.append(q1)
q2 = Question('Какого цвета нет на флаге России','Зеленый', 'Красный', 'Белый', 'Синий')
q3 = Question('Как называлась первая книга о Гарри Поттере', 'Филосовский камень', 'Узник Аскабана', 'Тайная комната', 'Кубок огня')
q4 = Question('1. Что из перечисленного сильнее всего влияет на восстановление организма?', 'Количество выпитого кофе', 'Качество сна', 'Просмотр новостей', 'Частота смены погоды')
q5 = Question(
    '2. Какой фактор чаще всего приводит к профессиональному выгоранию?',
    'Высокая нагрузка без восстановления',
    'Разнообразие задач',
    'Четкий рабочий график',
    'Поддержка коллег'
)
q6 = Question(
    '3. Что помогает дольше сохранять концентрацию при умственной работе?',
    'Работа без перерывов',
    'Короткие регулярные перерывы',
    'Многозадачность',
    'Постоянная проверка сообщений'
)
q7 = Question(
    '4. Какой навык наиболее важен для психологической устойчивости?',
    'Подавление эмоций',
    'Осознанное понимание своего состояния',
    'Игнорирование усталости',
    'Постоянная самокритика'
)
q8 = Question(
    '5. Что относится к активному восстановлению?',
    'Просмотр сериалов до глубокой ночи',
    'Легкая прогулка на свежем воздухе',
    'Дополнительная рабочая нагрузка',
    'Скроллинг соцсетей'
)
q9 = Question(
    '6. Какой признак чаще всего говорит о накопленной усталости?',
    'Рост продуктивности',
    'Стабильное настроение',
    'Раздражительность и снижение внимания',
    'Повышенная мотивация'
)
q10 = Question(
    '7. Что лучше всего помогает формировать устойчивые привычки?',
    'Резкие радикальные изменения',
    'Ожидание идеальных условий',
    'Небольшие регулярные действия',
    'Давление со стороны окружающих'
)
question_list.append(q10)
question_list.append(q9)


question_list.append(q8)
question_list.append(q7)
question_list.append(q6)
question_list.append(q2)
question_list.append(q3)
question_list.append(q4)
question_list.append(q5)
next_question()
otvet.clicked.connect(click_OK)
okno.show()

app.exec_()
#тестовое изменение 
