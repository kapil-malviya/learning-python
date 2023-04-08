# Generator : (understand with respect of time) ;



import random
import time

people = ['annaa', 'nitin', 'sumit', 'amit']
subject = ['python', 'django', 'sql']

def name_list(num_people):
	result = []
	for i in range(num_people):
		person = {'id':i,'name':random.choice(people),'subject':random.choices(subject)}
		result.append(person)
	return result


def people_generator(num_people):
	for i in range(num_people):
		person = {'id':i,'name':random.choice(people),'major':random.choices(subject)}
	yield person


t1 = time.time()
people = name_list(10000)
t2 = time.time()

print('took {}'.format(t2-t1))


t3 = time.time()
people = people_generator(10000000)
t4 = time.time()

print('took {}'.format(t4-t3))