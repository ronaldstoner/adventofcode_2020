# Day 4
import re

def checkPassportsPart1(passports):
    valid = 0
    requiredFields = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']

    for passport in passports:
        if all(fields in passport for fields in requiredFields):
            valid += 1
    return valid

def checkPassportsPart2(passports):
    valid = 0
    requiredFields = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']

    for passport in passports:

        #print(passport)
        if all(fields in passport for fields in requiredFields):
            valid_policies = [
                r'(byr:(19[2-8][0-9]|199[0-9]|200[0-2]))',
                r'(iyr:(201[0-9]|2020))',
                r'(eyr:(202[0-9]|2030))',
                r'(hgt:(1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)',
                r'(hcl:#([0-9]|[a-f]){6})',
                r'(ecl:(amb|blu|brn|gry|grn|hzl|oth))',
                r'(pid:\d{9}(?!\S))'
                ]
            if all(re.search(policy, passport) for policy in valid_policies):
                valid += 1
    return valid

# Main Loop
if __name__ == '__main__':

    passports = []

    with open('input.txt', 'r') as file:
        for line in file.read().split('\n\n'):
            line = line.strip()
            if line != '\n':
                passports.append(line.strip())

    # PART ONE
    valid = checkPassportsPart1(passports)
    print("\nPART ONE")
    print("Valid passports:", valid, "\n")

    # PART TWO
    valid = checkPassportsPart2(passports)
    print("PART TWO")
    print("Valid passports:", valid, "\n")
