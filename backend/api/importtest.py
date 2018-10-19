import csv
with open(r'C:\Users\Jacob\Documents\LaddrBase\laddr\backend\api\LolDuoCsv.csv','r') as f:
    reader = csv.reader(f)
    bios = list(reader)

print(len(bios))


N = 5
for test in range(N * 10):
    testlist = bios[test]
    print(testlist)


