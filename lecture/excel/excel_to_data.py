import django_excel as excel
import re

from lecture.models import Subject, Lecture, LectureTime
from university.models import CompletionDivision, Area

class LectureExcel(object):

    lecture_index = None
    lecture_index_numbers = None
    subject_index = None
    subject_index_numbers = None
    university_id = None

    # 인덱스 찾기위한 값 초기화
    def __init__(self):
        self.lecture_index = ['학수번호', '메인\n교수명', '강의실', '요일 및 교시',
                                  '년도', '학기', '개설대학', '개설학과전공']
        self.subject_index = ['학수번호', '교과목명', '이수\n구분', '선택영역', '학점']
        self.lecture_index_numbers = list()
        self.subject_index_numbers = list()

    def excel_process(self, file, university_id):
        print(file)
        print(university_id)
        data_array = self.get_excel_to_array(file)

        self.university_id = university_id

        # 엑셀에서 인덱스 위치 찾기
        self.get_index(data_array[0])

        for i in range(len(data_array)-1):
            data = data_array.pop()
            self.get_data(data)


    def get_excel_to_array(self, file):
        return excel.ExcelMixin.get_array(file)

    def get_data(self, data):
        self.get_subject(data[self.subject_index_numbers[0]['id']], data[self.subject_index_numbers[1]['id']],
                         data[self.subject_index_numbers[2]['id']], data[self.subject_index_numbers[3]['id']],
                         data[self.subject_index_numbers[4]['id']])
        self.get_lecture(data[self.lecture_index_numbers[0]['id']], data[self.lecture_index_numbers[1]['id']],
                         data[self.lecture_index_numbers[2]['id']], data[self.lecture_index_numbers[3]['id']],
                         data[self.lecture_index_numbers[4]['id']], data[self.lecture_index_numbers[5]['id']],
                         data[self.lecture_index_numbers[6]['id']], data[self.lecture_index_numbers[7]['id']])

    def get_subject(self, code, name, division_name, area_name, credit):

        #이미 있는지 체크
        if Subject.objects.filter(code=code).exists():
            print('이미있는 과목')
            return

        #이수구분, 영역 가져오기 (없으면 생성)
        division = None
        try:
            division = CompletionDivision.objects.get(university_id=self.university_id,
                                                         name=division_name)
        except CompletionDivision.DoesNotExist:
            division = CompletionDivision.objects.create(university_id=self.university_id,
                                                     name=division_name)

        area = None
        if area_name is not None:
            try:
                area = Area.objects.get(university_id=self.university_id,
                                        name=area_name)
            except Area.DoesNotExist:
                area = Area.objects.create(university_id=self.university_id,
                                           name=area_name)


        subject = Subject.objects.create(code=code, name=name, university_id=self.university_id,
                          completion_division=division, area=area, credit=credit)
        print('생성 완료 subject code='+code+' name='+name)

    def get_lecture(self, code, professor, class_room, class_time, year, semester,
                    college, department):

        #수정 필요 데이터 = 학과, 강의 시간
        #학과 데이터 수정 공백뒤 학과만 저장
        if ' ' in department:
            department = department.split(' ')[1]

        #강의시간 정규표현식으로 분리
        split_class_time = self.change_class_time(class_time)

        #강의가 이미 있는지 체크

        if Lecture.objects.filter(subject_id=code, professor=professor, class_room=class_room,
                                  opened_year=year, opened_semester=semester, opened_college=college,
                                  opened_department=department).exists():
            print('이미 있는 강의')
            return

        #저장 시작
        lecture_id = Lecture.objects.create(subject_id=code, professor=professor, class_room=class_room,
                                  opened_year=year, opened_semester=semester, opened_college=college,
                                  opened_department=department).id

        #시간 저장
        for class_time in split_class_time:
            LectureTime.objects.create(lecture_id=lecture_id, week=class_time[0], start_time=class_time[1],
                                       end_time=class_time[2])
        print('저장 완료')


    def get_index(self, index_line):

        for index_name in self.lecture_index:
            for i, name in enumerate(index_line):
                if name == index_name:
                    self.lecture_index_numbers.append({'id': i, 'name': name})
                    pass

        for index_name in self.subject_index:
            for i, name in enumerate(index_line):
                if name == index_name:
                    self.subject_index_numbers.append({'id': i, 'name': name})
                    pass

    def change_class_time(self, class_time):
        class_time = class_time.replace(',', ' ')

        week_days = class_time
        week_days = re.sub('[0-9][0-9]:[0-9][0-9]~[0-9][0-9]:[0-9][0-9]', 'T', week_days)
        week_days = re.sub('[0-9][0-9]:[0-9][0-9]-[0-9][0-9]:[0-9][0-9]', 'T', week_days)
        week_days = week_days.replace(' ', '')

        rex = re.compile('[0-9][0-9]:[0-9][0-9]')
        timetable = re.findall(rex, class_time)
        # print(timetable)
        # print(week_days)

        split_class_time = list()
        time_index = 0
        for week in range(len(week_days)):
            if week_days[week] == 'T':
                # print("Time Change")
                time_index += 2
                pass
            else:
                split_class_time.append([week_days[week], timetable[time_index], timetable[time_index + 1]])
                # print('week=' + week_days[week] + ' time=' + timetable[time_index] + '~' + timetable[time_index + 1])
        return split_class_time