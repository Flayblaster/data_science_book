from collections import defaultdict
import matplotlib.pyplot as plt

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

y = [(salaries[0]) for salaries in salaries_and_tenures]
x = [(tenures[1]) for tenures in salaries_and_tenures]

plt.scatter(x, y)
plt.title('Salário por Anos de Experiência')
plt.xlabel('Anos de Experiência')
plt.ylabel('Salário')
#plt.show()

#Analizing the average salary by year of experience
salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)
print(salary_by_tenure)

#The key are year, each value is the average salary associate by the tenure
average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}
print(average_salary_by_tenure)

#Buckets of tenure
def tenure_bucket(tenure):
    if tenure < 2:
        return 'less than 2'
    elif tenure < 5:
        return 'between two and five'
    else:
        return 'more than five'

#The keys are buckets of tenure and the values are lists of salaries associate with the bucket in question
salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

#The keys are buckets of tenure and the values are the average salary in the bucket
average_salary_by_bucket = {
    tenure_bucket: sum(salaries) / len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}
for bucket, avg in average_salary_by_bucket.items():
    print(f'{bucket}:', avg)