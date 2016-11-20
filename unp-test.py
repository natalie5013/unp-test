import sys, csv
# import msvcrt

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

class KeyTableReader:


	def __init__(self, filename):
		self.keys = []
		for i in range(90):
			self.keys.append(0)

		csvfile = open(filename, 'rb')
		rows = csv.reader(csvfile, delimiter=';')
		for row in rows:
			for i in range(3):
				# row: 5;2;2;35;8;-2;65;1;-3
				num = int(row[i*3+0])
				yes =     row[i*3+1]
				no =      row[i*3+2]
				# 5;2;2
				if is_number(yes):
					yes = int(yes) 
				if is_number(no):
					no = int(no) 
				a = {'num': num, 'yes': yes, 'no': no}
				num = a['num']
				# print a
				self.keys[num-1] = a

		for i in range(len(self.keys)):
			k = self.keys[i]
			if k == 0:
				print 'ERROR: MISSING KEY: ', (i+1)

class AnketaReader:

	def __init__(self, filename):
		file = open(filename, 'rb')
		self.answers = []
		lines = file.readlines()
		for line in lines:
			line = line.strip()
			# print line
			if len(line) > 0:
				if line == 'y':
					# print 'YES'
					self.answers.append(True)
				elif line == 'n':
					# print 'NO'
					self.answers.append(False)
				else:
					print 'ERROR: ', line


class Processor:

	def process(self, anketa, keytab):
		result = 0
		for i in range(len(anketa.answers)):
			a = anketa.answers[i]
			k = keytab.keys[i]
			if a:
				res = k['yes']					
			else:
				res = k['no']					

			# print str(i), ': ', a, k, res
			
			if is_number(res):
				result += res
				# print str(i+1), ': ', a, k, '\t', res, '\t', result
			# else:
				# print str(i+1), ': ', a, k, 'missed'
		return result

def usage():
	print 'Usage:'
	print '  m/w file'
	sys.exit()

				
keytab1 = KeyTableReader('test-unp1.csv')
keytab2 = KeyTableReader('test-unp2.csv')
keytab3 = KeyTableReader('test-unp3.csv')
keytab4 = KeyTableReader('test-unp4.csv')

man = [keytab1, keytab3]
woman = [keytab2, keytab4]

processor = Processor()

if len(sys.argv) <= 2:
	usage()

if sys.argv[1] == 'm':
	keytabs = man
elif sys.argv[1] == 'w':
	keytabs = woman
else:
	usage()

filename = sys.argv[2]

anketa = AnketaReader(filename)

res1 = processor.process(anketa, keytabs[0])
res2 = processor.process(anketa, keytabs[1])

print '  neurotic   : ', res1
print '  psychopatic: ', res2

