import pandas as pd 
import random
import sqlite3

# БЛОК 1. Переменные и т.д

id_cheek = 0
citizen_cheek = 1000
citizen_taimer = 0

city = ('Forbdon', 'Sautburg', 'Edbyrg', 'Boymoyt')

work_place_list = []
citizen_list = []
years_born_list = []
years_old_list = []
name_id_list = []
gender_list = []
home_list = []
status_list = []
date = []
work_list = []

kindergarten_1 = {'name': 'A_KIND', 'places': 300, 'free_places': 300, 'location': 'Forbdon', 'type': 'kindergarten'}
kindergarten_2 = {'name': 'B_KIND', 'places': 400, 'free_places': 400, 'location': 'Sautburg', 'type': 'kindergarten'}
kindergarten_3 = {'name': 'C_KIND', 'places': 200, 'free_places': 200, 'location': 'Edbyrg', 'type': 'kindergarten'}
kindergarten_4 = {'name': 'D_KIND', 'places': 250, 'free_places': 250, 'location': 'Boymoyt', 'type': 'kindergarten'}
kindergarten_5 = {'name': 'F_KIND', 'places': 300, 'free_places': 300, 'location': 'Forbdon', 'type': 'kindergarten'}

school_1 = {'name': 'A_SCHO', 'places': 100, 'free_places': 100, 'location': 'Forbdon', 'type': 'school'}
school_2 = {'name': 'B_SCHO', 'places': 300, 'free_places': 300, 'location': 'Sautburg', 'type': 'school'}
school_3 = {'name': 'C_SCHO', 'places': 250, 'free_places': 250, 'location': 'Edbyrg', 'type': 'school'}
school_4 = {'name': 'D_SCHO', 'places': 600, 'free_places': 600, 'location': 'Boymoyt', 'type': 'school'}
school_5 = {'name': 'F_SCHO', 'places': 200, 'free_places': 200, 'location': 'Forbdon', 'type': 'school'}

job_1 = {'name': 'A_JOB', 'places': 2000, 'free_places': 2000, 'location': 'Forbdon', 'type': 'job'}
job_2 = {'name': 'B_JOB', 'places': 3000, 'free_places': 3000, 'location': 'Sautburg', 'type': 'job'}
job_3 = {'name': 'C_JOB', 'places': 5000, 'free_places': 5000, 'location': 'Edbyrg', 'type': 'job'}
job_4 = {'name': 'D_JOB', 'places': 6000, 'free_places': 6000, 'location': 'Boymoyt', 'type': 'job'}
job_5 = {'name': 'F_JOB', 'places': 2000, 'free_places': 2000, 'location': 'Forbdon', 'type': 'job'}

work_place_list.append(kindergarten_1)
work_place_list.append(kindergarten_2)
work_place_list.append(kindergarten_3)
work_place_list.append(kindergarten_4)
work_place_list.append(kindergarten_5)

work_place_list.append(school_1)
work_place_list.append(school_2)
work_place_list.append(school_3)
work_place_list.append(school_4)
work_place_list.append(school_5)

work_place_list.append(job_1)
work_place_list.append(job_2)
work_place_list.append(job_3)
work_place_list.append(job_4)
work_place_list.append(job_5)

# БЛОК 2. Классы и функции

def creater_yers_born():
    born_date = random.randint(1100, 1165)
    return(born_date)

def creater_id_name():
    global id_cheek
    id_cheek += 1
    return(id_cheek)

def creater_gender():
    random_gender = random.choice(['Male', 'Female'])
    return(random_gender)

def years_vis(years_born):
    years_old = 1165 - years_born
    return(years_old)

def status_locate(years_old):
    if years_old < 14:
        return('child')
    if years_old < 18:
        return('teenager')
    if years_old < 50:
        return('adult')
    else:
        return('old')

def home_locate():
    return(random.choice(city))
# РАБОТА 
def work_place_locate(status, home, work_place_list):
    if status == 'child':
        if home == 'Forbdon':
                for work_place in work_place_list:
                    if (work_place.get('location')) == 'Forbdon' and (work_place.get('type')) == 'kindergarten' and (work_place.get('free_places')) >= 1:
                        work_place['free_places'] -= 1
                        return((work_place.get('name')))
                        break
                    else:
                        try:
                            del(work_place)
                        except:
                            return('without_place')  

        if home == 'Sautburg':
                for work_place in work_place_list:
                    if (work_place.get('location')) == 'Sautburg' and (work_place.get('type')) == 'kindergarten' and (work_place.get('free_places')) >= 1:
                        work_place['free_places'] -= 1
                        return((work_place.get('name')))
                        break
                    else:
                        try:
                            del(work_place)
                        except:
                            return('without_place')  
        if home == 'Edbyrg':
                for work_place in work_place_list:
                    if (work_place.get('location')) == 'Edbyrg' and (work_place.get('type')) == 'kindergarten' and (work_place.get('free_places')) >= 1:
                        work_place['free_places'] -= 1
                        return((work_place.get('name')))
                        break
                    else:
                        try:
                            del(work_place)
                        except:
                            return('without_place')  
        if home == 'Boymoyt':
                for work_place in work_place_list:
                    if (work_place.get('location')) == 'Boymoyt' and (work_place.get('type')) == 'kindergarten' and (work_place.get('free_places')) >= 1:
                        work_place['free_places'] -= 1
                        return((work_place.get('name')))
                        break
                    else:
                        try:
                            del(work_place)
                        except:
                            return('without_place')
    if status == 'teenager':
        if home == 'Forbdon':
                for work_place in work_place_list:
                    if (work_place.get('location')) == 'Forbdon' and (work_place.get('type')) == 'school' and (work_place.get('free_places')) >= 1:
                        work_place['free_places'] -= 1
                        return((work_place.get('name')))
                        break
                    else:
                        try:
                            del(work_place)
                        except:
                            return('without_place')  

        if home == 'Sautburg':
                for work_place in work_place_list:
                    if (work_place.get('location')) == 'Sautburg' and (work_place.get('type')) == 'school' and (work_place.get('free_places')) >= 1:
                        work_place['free_places'] -= 1
                        return((work_place.get('name')))
                        break
                    else:
                        try:
                            del(work_place)
                        except:
                            return('without_place')  
        if home == 'Edbyrg':
                for work_place in work_place_list:
                    if (work_place.get('location')) == 'Edbyrg' and (work_place.get('type')) == 'school' and (work_place.get('free_places')) >= 1:
                        work_place['free_places'] -= 1
                        return((work_place.get('name')))
                        break
                    else:
                        try:
                            del(work_place)
                        except:
                            return('without_place')  
        if home == 'Boymoyt':
                for work_place in work_place_list:
                    if (work_place.get('location')) == 'Boymoyt' and (work_place.get('type')) == 'school' and (work_place.get('free_places')) >= 1:
                        work_place['free_places'] -= 1
                        return((work_place.get('name')))
                        break
                    else:
                        try:
                            del(work_place)
                        except:
                            return('without_place')      
    if status == 'adult':
        if home == 'Forbdon':
                for work_place in work_place_list:
                    if (work_place.get('location')) == 'Forbdon' and (work_place.get('type')) == 'job' and (work_place.get('free_places')) >= 1:
                        work_place['free_places'] -= 1
                        return((work_place.get('name')))
                        break
                    else:
                        try:
                            del(work_place)
                        except:
                            return('without_place')


        if home == 'Sautburg':
                for work_place in work_place_list:
                    if (work_place.get('location')) == 'Sautburg' and (work_place.get('type')) == 'job' and (work_place.get('free_places')) >= 1:
                        work_place['free_places'] -= 1
                        return((work_place.get('name')))
                        break
                    else:
                        try:
                            del(work_place)
                        except:
                            return('without_place')

        if home == 'Edbyrg':
                for work_place in work_place_list:
                    if (work_place.get('location')) == 'Edbyrg' and (work_place.get('type')) == 'job' and (work_place.get('free_places')) >= 1:
                        work_place['free_places'] -= 1
                        return((work_place.get('name')))
                        break
                    else:
                        try:
                            del(work_place)
                        except:
                            return('without_place')
        if home == 'Boymoyt':
                for work_place in work_place_list:
                    if (work_place.get('location')) == 'Boymoyt' and (work_place.get('type')) == 'job' and (work_place.get('free_places')) >= 1:
                        work_place['free_places'] -= 1
                        return((work_place.get('name')))
                        break
                    else:
                        try:
                            del(work_place)
                        except:
                            return('without_place')  
    else:
         return('Retired')

class Citizen():
# Иницализация данных о жители
    def __init__ (self, name_id, years_born, years_old, home, gender, status, work_place):
        self.name_id = name_id
        self.years_born = years_born
        self.years_old = years_old
        self.home = home
        self.gender = gender
        self.status = status
        self.work_place = work_place
# Информация о жители
    def information(self):
        print(f'User name - {self.name_id}')
        print(f'User years - {self.years_born}')
        print(f'User old - {self.years_old}')
        print(f'User live in - {self.home}')
        print(f'User gender - {self.gender}')
        print(f'User status - {self.status}')
        print(f'User work in - {self.work_place}')
        print('\n---------------------------')
    def home_information(self):
        return(self.home)


while citizen_taimer != citizen_cheek:
    name_id = creater_id_name()
    years_born = creater_yers_born()
    years_old = years_vis(years_born)
    home = home_locate()
    gender = creater_gender()
    status = status_locate(int(years_old))
    work_place = work_place_locate(status, home, work_place_list)
    citizen_anket = Citizen(name_id, years_born, years_old, home, gender, status, work_place)
    citizen_list.append(citizen_anket)
    citizen_taimer += 1
    gender_list.append(getattr(citizen_list[-1],'gender'))
    name_id_list.append(getattr(citizen_list[-1],'name_id'))
    years_born_list.append(getattr(citizen_list[-1],'years_born'))
    years_old_list.append(getattr(citizen_list[-1],'years_old'))
    home_list.append(getattr(citizen_list[-1],'home'))
    status_list.append(getattr(citizen_list[-1],'status'))
    work_list.append(getattr(citizen_list[-1],'work_place'))
    # citizen_anket.information()

date.append(gender_list)
date.append(name_id_list)
date.append(years_born_list)
date.append(years_old_list)
date.append(home_list)
date.append(status_list)
date.append(work_list)

data = {'ID': name_id_list, 'Years_born': years_born_list, 'Years_old': years_old_list, 'Home': home_list,
'Gender': gender_list,'Status': status_list, 'Work': work_list} 
df = pd.DataFrame(data)
conn = sqlite3.connect('my_database.db')
df.to_sql('citizen_list', conn, if_exists='replace', index=False)
print(df)
conn.close()

