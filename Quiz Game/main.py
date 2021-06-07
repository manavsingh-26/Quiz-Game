from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    ques_text = question["question"]
    ques_answer = question["correct_answer"]
    new_ques = Question(ques_text,ques_answer)
    question_bank.append(new_ques)
    
quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_ques()
    
    
print("You completed the Quiz!!")
print(f"Your final score is: {quiz.score}/{quiz.ques_no}")