import sys

with open(sys.argv[1], 'r') as f:
    test_cases = f.read().splitlines()

digit2number = {
    'a' : 0,
    'b' : 1,
    'c' : 2,
    'd' : 3,
    'e' : 4,
    'f' : 5,
    'g' : 6,
    'h' : 7,
    'i' : 8,
    'j' : 9,
    '0' : 0,
    '1' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
}

for test in test_cases:
    text = ''.join(str(digit2number.get(i, '')) for i in test)
    print text if text else 'NONE'
