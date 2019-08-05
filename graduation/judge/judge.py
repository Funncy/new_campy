from student.models import StudentInfo, StudentAddedMajor
from history.models import LectureHistory

from graduation.models import RuleGeneral

from .track import track
from .rule_factory import rule_factory

class Judge:

    def __init__(self):
        self.rule_result = None
        self.subject_list = None
        self.rule_list = None
        self.student = None
        self.add_major = None
        self.tracks = None

    # 초기 데이터 셋팅 (학생정보, 과목정보, 룰정보)
    def set_data(self, student_id):
        # 학생 정보 로드
        self.student = StudentInfo.objects.get(user_id=student_id)
        self.add_major = StudentAddedMajor.objects.filter(user_id=student_id)
        # 학생 수강 정보 로드
        self.subject_list = LectureHistory.objects.filter(user_id=student_id)
        # 학생 정보에 맞는 트랙호출 및 트랙별 룰 호출
        #self.rule_list = track(self.student, self.add_major).get_rule_list()
        print(self.rule_list)

    # 졸업 판정 진행
    def judging(self):

        # 판정 진행을 해야하는 과목들
        checked_subject_list = None

        self.rule_list = RuleGeneral.objects.filter(university=self.student.university)

        # 룰 수정 진행
        result = list()




        # 룰 별 판정 진행
        for rule in self.rule_list:
            #룰에 맞는 과목들 가져오기
            checked_subject_list = self.compare_subject_and_group(rule)
            print(checked_subject_list)
            #룰 별 판정 진행
            rule_result = rule_factory.createRule(rule, checked_subject_list, university_grade).assess()
            result.append(rule_result)
        return result






    def compare_subject_and_group(self, rule):

        #매핑 데이터 꺼내기
        mappings = rule['rule_subject_group']

        # 과목 그룹에 해당 되는 과목 담기
        checked_subject_list = list()

        #과목 순회
        for subject in self.subject_list:
            for mapping in mappings:
                if mapping['mappings__mapping_completion_division'] != '':
                    print(subject)
                    print(mapping['mappings__mapping_completion_division'])
                    if subject['history_subject_complete_division'] == mapping['mappings__mapping_completion_division']:
                        checked_subject_list.append(subject)
                elif mapping['mappings__mapping_area'] != '':
                    print(mapping['mappings__mapping_area'])
                    if subject['history_subject_area'] == mapping['mappings__mapping_area']:
                        checked_subject_list.append(subject)
        return checked_subject_list