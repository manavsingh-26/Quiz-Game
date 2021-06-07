class QuizBrain:
    def __init__(self,ques_list):
        self.ques_no =0
        self.ques_list = ques_list
        self.score=0
        
    def next_ques(self):
        curr_ques = self.ques_list[self.ques_no]
        self.ques_no+=1
        
        user_answer = input(f"Q.{self.ques_no}:{curr_ques.text} (True/False)")
        self.check_answer(user_answer,curr_ques.answer)
    
    def check_answer(self,user_answer,corr_answer):
        if user_answer.lower() == corr_answer.lower():
            print("You are right!")
            self.score+=1
            
        else:
            print("Wrong answer!!")
        print(f"The correct answer: {corr_answer}")
        print(f"Your current Score: {self.score}/{self.ques_no}")    
        print("\n")
    
    def still_has_question(self):
        return self.ques_no < len(self.ques_list)
         
         
        