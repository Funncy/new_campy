from graduation.models import RuleSpecific, RuleGeneral

class track:

    def __init__(self, student, add_major):
        self.track_name = None
        self.tracks = None
        self.rules = None
        self.student = student
        self.add_major = add_major
        self.admission_year = None
        self.university_name = None

    def get_general_rule_list(self):

        rule_list = list()

        self.admission_year = self.student.admission_year
        self.university_name = self.student.university.name

        print(self.university_name)

        # 공통 트랙 general 데이터 가져오기
        rule_list.extend(self.get_general_rule_by_university_and_track('공통'))



    def get_general_rule_by_university_and_track(self, track):

        rules = RuleGeneral.objects.filter(university=self.student.university, track=track)

        return rules
