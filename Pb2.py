def isYearLeap(year):
    return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0));

zie_luni_normal = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
zile_luni_bisect = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def daysInMonth(year, month):
    if isYearLeap(year):
        return zile_luni_bisect[month]
    return zie_luni_normal[month]

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 5, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
    yr = testYears[i]
    mo = testMonths[i]
    print(yr, mo, "->", end="")
    result = daysInMonth(yr, mo)
    if result == testResults[i]:
        print("OK")
    else:
        print("Failed")

print(daysInMonth(2015, 2))