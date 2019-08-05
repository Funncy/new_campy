from .rule_type import rule_type
from .rule_type_1 import rule_type_1
from .rule_type_2 import rule_type_2

class rule_factory:

    @staticmethod
    def createRule(rule, subject_list, university_grade):
        if rule['rule_type'] == '1':
            return rule_type_1(rule, subject_list, university_grade)
        elif rule['rule_type'] == '2':
            return rule_type_2(rule, subject_list, university_grade)
        elif rule['rule_type'] == '3':
            return rule_type_1(rule, subject_list, university_grade)
        elif rule['rule_type'] == '4':
            return rule_type_1(rule, subject_list, university_grade)
        elif rule['rule_type'] == '5':
            return rule_type_1(rule, subject_list, university_grade)
        return None