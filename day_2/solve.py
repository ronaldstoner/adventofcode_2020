# Day 2

def CheckPasswords(A):
    valid = 0
    for line in A:
        min_val = line.split("-")[0]
        max_val = line.split("-")[1].split(" ")[0]
        expect_char = line.split(":")[0].split(" ")[1]
        passphrase = line.split(":")[1].split(" ")[1]
        result = passphrase.count(expect_char)
        
        if (int(result) >= int(min_val)):
            if (int(result) <= int(max_val)):
                valid += 1

    return valid

def CheckPassPosition(A):
    valid = 0
    for line in A:
        fir_pos = int(line.split("-")[0]) - 1
        sec_pos = int(line.split("-")[1].split(" ")[0]) - 1
        expect_char = line.split(":")[0].split(" ")[1]
        passphrase = line.split(":")[1].split(" ")[1]

        if passphrase[int(sec_pos)] != expect_char:
            if passphrase[int(fir_pos)] == expect_char:
                valid += 1
        
        if passphrase[int(fir_pos)] != expect_char:
            if passphrase[int(sec_pos)] == expect_char:
                valid += 1

    return valid

# Main Loop
if __name__ == '__main__':

    #Read input into list line by line
    with open("input.txt") as file:
        input_dic = [l.rstrip("\n") for l in file]

        # Sort for efficiency
        input_dic.sort()

        # PART ONE
        valid = CheckPasswords(input_dic)
        print("PART ONE")
        print("Valid passwords:", valid, "\n")        
        
        # PART TWO
        valid = CheckPassPosition(input_dic)
        print("PART TWO")
        print("Valid passwords:", valid, "\n")
