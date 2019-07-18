import re


def test():
    class_time = '월수13:30-15:00,목13:30-15:00'
    class_time = class_time.replace(',', ' ')

    week_days = class_time
    week_days = re.sub('[0-9][0-9]:[0-9][0-9]~[0-9][0-9]:[0-9][0-9]', 'T', week_days)
    week_days = re.sub('[0-9][0-9]:[0-9][0-9]-[0-9][0-9]:[0-9][0-9]', 'T', week_days)
    week_days = week_days.replace(' ', '')

    rex = re.compile('[0-9][0-9]:[0-9][0-9]')
    timetable = re.findall(rex, class_time)
    time_result_list = []
    print(timetable)
    print(week_days)

    split_class_time = list()
    time_index = 0
    for week in range(len(week_days)):
        if week_days[week] == 'T':
            print("Time Change")
            time_index += 2
            pass
        else:
            split_class_time.append([week_days[week], timetable[time_index], timetable[time_index+1]])
            print('week='+week_days[week]+' time='+timetable[time_index]+'~'+timetable[time_index+1])
    print(split_class_time)
    pass

test()