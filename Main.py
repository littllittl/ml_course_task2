import pandas
import re

def clean_name(name):
    s = re.search('^[^,]+, (.*)', name)
    if s:
        name = s.group(1)
    s = re.search('\(([^)]+)\)', name)
    if s:
        name = s.group(1)
    name = re.sub('(Miss\. |Mrs\. |Ms\. )', '', name)
    name = name.split(' ')[0].replace('"', '')
    return name

data = pandas.read_csv('titanic.csv', index_col='PassengerId')
data['Pclass'] = data['Pclass'].astype(object)

# 1. Какое количество мужчин и женщин ехало на корабле? В качестве ответа приведите два числа через пробел.
sex_counts = data['Sex'].value_counts()
first = open('first.txt', 'w')
first.write( f'{sex_counts["male"]} {sex_counts["female"]}')

# 2. Какой части пассажиров удалось выжить? Посчитайте долю выживших пассажиров.
# Ответ приведите в процентах (число в интервале от 0 до 100, знак процента не нужен).
surv_counts = data['Survived'].value_counts()
surv_percent = 100.0 * surv_counts[1] / surv_counts.sum()
second = open('second.txt', 'w')
second.write('{:0.2f}'.format(surv_percent))

# 3. Какую долю пассажиры первого класса составляли среди всех пассажиров?
# Ответ приведите в процентах (число в интервале от 0 до 100, знак процента не нужен).
pclass_counts = data['Pclass'].value_counts()
pclass_percent = 100.0 * pclass_counts[1] / pclass_counts.sum()
third = open('third.txt', 'w')
third.write('{:0.2f}'.format(pclass_percent))

# 4. Какого возраста были пассажиры? Посчитайте среднее и медиану возраста пассажиров.
ages = data['Age'].dropna()
fourth = open('fourth.txt', 'w')
fourth.write("{:0.2f} {:0.2f}".format(ages.mean(), ages.median()))

# 5. Коррелируют ли число братьев/сестер с числом родителей/детей?
# Посчитайте корреляцию Пирсона между признаками SibSp и Parch.
corr =data["SibSp"].corr(data["Parch"])
fifth = open('fifth.txt', 'w')
fifth.write("{:0.2f}".format(corr))

# 6. Какое самое популярное женское имя на корабле? Извлеките из полного имени пассажира (колонка Name)
# его личное имя (First Name).
fn = data[data['Sex'] == 'female']['Name']
name = fn.map(clean_name)
name_counts = name.value_counts()
sixth = open('sixth.txt', 'w')
sixth.write(name_counts.index.values[0])
