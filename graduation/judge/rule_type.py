from abc import ABCMeta, abstractmethod

class rule_type(metaclass=ABCMeta):
    rule = None
    subject_list = None

    def __init__(self, rule, subject_list, university_grade):
        self.rule = rule
        self.subject_list = subject_list
        self.unviersity_grade = university_grade

    '''
    각 룰 타입 별로
    졸업 판정 진행
    '''
    @abstractmethod
    def assess(self):
        pass

    '''
    4.5 A+ A0 B+ B0 C+ C0 D+ D0 F
    4.3 A+ A0 A- B+ B0 B- C+ C0 C- D+ D0 D- F
    4.0 A B C D
    '''
    def is_pass_npass(self, student_grade):
        if student_grade == 'P' or student_grade == 'NP':
            return True
        else:
            return False

    def change_grade_to_credit(self, student_grade):
        #pass npass
        if student_grade == 'P':
            return 1
        elif student_grade == 'NP':
            return 0

        if self.unviersity_grade['maximum'] == '4.5':
            return self.calculate_grade_4dot5(student_grade)
        elif self.unviersity_grade['maximum'] == '4.3':
            return self.calculate_grade_4dot3(student_grade)
        elif self.unviersity_grade['maximum'] == '4.0':
            return self.calculate_grade_4dot0(student_grade)
        return None

    # 4.5 계산
    def calculate_grade_4dot5(self, student_grade):
        if student_grade == 'A+':
            return 4.5
        elif student_grade == 'A0':
            return 4.0
        elif student_grade == 'B+':
            return 3.5
        elif student_grade == 'B0':
            return 3.0
        elif student_grade == 'C+':
            return 2.5
        elif student_grade == 'C0':
            return 2.0
        elif student_grade == 'D+':
            return 1.5
        elif student_grade == 'D0':
            return 1.0
        return 0

    def calculate_grade_4dot3(self, student_grade):
        if student_grade == 'A+':
            return 4.3
        elif student_grade == 'A0':
            return 4.0
        elif student_grade == 'A-':
            return 3.7
        elif student_grade == 'B+':
            return 3.3
        elif student_grade == 'B0':
            return 3.0
        elif student_grade == 'B-':
            return 2.7
        elif student_grade == 'C+':
            return 2.3
        elif student_grade == 'C0':
            return 2.0
        elif student_grade == 'C-':
            return 1.7
        elif student_grade == 'D+':
            return 1.3
        elif student_grade == 'D0':
            return 1.0
        elif student_grade == 'D-':
            return 0.7
        return 0

    def calculate_grade_4dot0(self, student_grade):
        if student_grade == 'A':
            return 4.0
        elif student_grade == 'B':
            return 3.0
        elif student_grade == 'C':
            return 2.0
        elif student_grade == 'D':
            return 1.0
        return 0