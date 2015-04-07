import sys
with open(sys.argv[1], 'r') as f:
    test_cases = f.read().splitlines()

for test in test_cases:
    if len(test):
	test = test.split(',')
	test[1] = test[1].strip()
	for i in test[1]:
	    test[0] = test[0].replace(i, "")
	print test[0]
