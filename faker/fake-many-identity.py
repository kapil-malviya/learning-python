from faker import Faker
fake = Faker()

for x in range(8):
	print('Employee name : ', fake.name())
	print('Employee First Name : ', fake.first_name())
	print('Employee Last Name : ', fake.last_name())
	print('Employee DOB : ', fake.date())
	print('Employee ID : ', fake.random_number(5))
	print('Employee mail ID : ', fake.email())
	print('Employee contact number : ', fake.random_int(min=6000000000, max=9999999999))
	print('Employee Role : ', fake.random_element(elements=('Software Engineer', 'Team Lead', 'Project Manager', 'Project Lead')))
	print('--------')