from question import Question
from quiz import Quiz

if __name__ == '__main__':
    q1 = Question('En iyi programlama dili?',['C#','Python','Java','Javascript'],'Python')
    q2 = Question('En sevilen programlama dil?',['C#','Python','Java','Javascript'],'Java')
    q3 = Question('En kolay programlama dil?',['C#','Python','Java','Javascript'],'C#')

    questions = [q1,q2,q3]

    quiz = Quiz(questions)
    quiz.load_question()
