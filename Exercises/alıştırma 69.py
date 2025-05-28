class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    def checkAnswer(self,answer):
        return self.answer==answer


class Quiz:
    def __init__(self,questions):
        self.questions=questions
        self.score=0

q1 = Question(
    text="En iyi programlama dili hangisidir?",
    choices=["C#", "python,", "javascript", "java"],
    answer="python"
)
q2 = Question(
    text="En popüler programlama dili hangisidir?",
    choices=["javascript", "python,", "java", "C#"],
    answer="python"
)
q3 = Question(
    text="En çok kazandıran programlama dili hangisidir?",
    choices=["python", "java,", "javascript", "C#"],
    answer="python"
)
questions =[q1,q2,q3]
