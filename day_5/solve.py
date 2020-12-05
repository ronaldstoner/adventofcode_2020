# Day 5

def crunchSeats(seat_dic):
    highest_seat_id = 0

    for line in seat_dic:
        seat_id = "".join(['0' if char == "F" or char == "L" else '1' for char in line])
        highest_seat_id = max(int(seat_id, 2), highest_seat_id)

    return highest_seat_id

def findMySeat(seat_dic):

    seat_list = []

    for line in seat_dic:
        seat_id = "".join(['0' if char == "F" or char == "L" else '1' for char in line])
        row = int(seat_id[:7], 2)
        col = int(seat_id[7:], 2)
        seat_list.append(int(row * 8 + col))
    return seat_list

def Diff(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif

# Main Loop
if __name__ == '__main__':

    #Read input into list line by line
    with open("input.txt") as file:

        seat_dic = [l.rstrip("\n") for l in file]

        # PART ONE
        highest_seat = crunchSeats(seat_dic)
        print("\nPART ONE")
        print("Highest Seat ID:", highest_seat, "\n")

        # PART TWO
        seat_list = findMySeat(seat_dic)
        seat_list.sort()

        for (i,n) in enumerate(seat_list):
            if seat_list[i+1] != n + 1:
                seat = n + 1
                break

        print("PART TWO")
        print("My Seat:", seat, '\n')
