import sys, csv
import msvcrt
        
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


answers = []

for i in range(90):
	answers.append(0)

with open('test-unp2.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=';')
	for row in reader:
		for i in range(3):
			yes = row[i*3+1]
			no = row[i*3+2]
			# if yes.isnumeric():
				# yes = int(yes) 
			if is_number(yes):
				yes = int(yes) 
			if is_number(no):
				no = int(no) 
			# if no.isnumeric():
				# no = int(no) 
			a = {'num': int(row[i*3]), 'yes': yes, 'no': no}
			num = a['num']
			#print num	
			answers[num-1] = a

for a in answers:
	print 'answer: ', a

result = 0

for i in range(1, 90, 2):
	a = answers[i]
	sys.stdout.write('Question ' + str(a['num']) + ': \r')
	ch = msvcrt.getch()
	if ch == 'x' or ch == 'q':
		exit(0)
	delta = 0
	ans = ''		
	if ch == 'y' or ch == '[':
		delta = a['yes']
		ans = 'YES'
	elif ch == 'n' or ch == ']':
		delta = a['no']
		ans = 'NO '
	
	if is_number(delta):
		result = result + delta
		sys.stdout.write('Question ' + str(a['num']) + ': result: '  + ' ' + str(result) + ' ' + str(ans) + '(' + str(delta) + ')                           \r')
	else:
		print 'DELTA: ', delta		
