import string, random, sys

def genPass(numChars, usePunc):
	chars = string.ascii_letters + string.digits
	if usePunc:
		chars = chars + string.punctuation
	password = ''
	for i in range(numChars):
		password = password + random.choice(chars)
	return password

def isInteger(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

def usage():
	print('Usage:\ngenerate_password.py [-noPunc] numchars')

def main(args):
	if len(args) > 2 or len(args) < 1:
		usage()
		return
	if ((len(args) == 2 and (args[0] != '-noPunc' or not isInteger(args[1]))) or
		(len(args) == 1 and not isInteger(args[0]))):
		usage()
		return
	numChars = int(args[-1])
	usePunc = args[0] != '-noPunc'
	print(genPass(numChars, usePunc))

main(sys.argv[1:])