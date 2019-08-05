from .rule_type import rule_type

'''
첫번째 룰 타입
평균 평점
'''
class rule_type_2(rule_type):

    def assess(self):
        result = dict()
        subject_value = 0.0
        print(self.subject_list)
        print(self.rule)

        for subject in self.subject_list:
            subject_value += float(subject['history_subject_credit'])

        #평균 평점
        subject_value /= len(self.subject_list)
        print(subject_value)

        # 결과 저장
        if subject_value >= float(self.rule['rule_value']):
            result['result'] = 'true'
        else:
            result['result'] = 'false'

        result['rule_name'] = self.rule['rule_name']
        result['rule_track'] = self.rule['rule_track']
        result['max_value'] = int(self.rule['rule_value'])
        result['current_value'] = subject_value
        result['subject_list'] = self.subject_list

        return result