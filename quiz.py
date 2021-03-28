class Quiz:
    '''
    input = List
    '''
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.question_index = 0

    def get_question(self):
        return self.questions[self.question_index]
    
    def display_question(self):
        question = self.get_question()
        print(f'Soru {self.question_index + 1}: {question.text}')

        for q in question.choices:
            print(f'-{q}')
        
        answer = input('answer: ')
        self.guess(answer)
        self.load_question()

    def guess(self,answer):
        question = self.get_question()

        if question.check_answer(answer):
            self.score += 1
        
        self.question_index += 1
    
    def load_question(self):
        if len(self.questions) == self.question_index:
            self.show_score()
        else:
            self.display_progress()
            self.display_question()
    
    def show_score(self):
        print(f'score: {self.score}')
    
    def display_progress(self):
        total_question = len(self.questions)
        question_number = self.question_index + 1

        if question_number > total_question:
            print('Finished quiz')
        else:
            print(f'Question {question_number} of {total_question}'.center(100,'*'))