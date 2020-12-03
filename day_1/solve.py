# Day 1

# PART ONE - Find two numbers
def find2Numbers(A, sum):
    for x in A:
    #print("Value of x: ", x)

    # Start crunching
        for line in A:
            test_answer = int(x) + int(line)
            #print(test_answer)
            if test_answer == sum:
                print("PART ONE")
                print("You did it!       x=", x, "y=", int(line))
                print("Solution:        ", (int(x)*int(line)), "\n")
                return True

# PART TWO - Find three numbers
def find3Numbers(A, arr_size, sum): 
  
    for i in range(0, arr_size-2): 
        
        l = i + 1 
        r = arr_size-1 
        
        while (l < r): 
          
            if((int(A[i]) + int(A[l]) + int(A[r])) == sum): 
                print("PART TWO")
                print("You did it!       i=", A[i], ' l=', A[l], ' r=', A[r])
                print("Solution:        ", (int(A[i]) * int(A[l]) * int(A[r])))
                return True
              
            elif ((int(A[i]) + int(A[l]) + int(A[r])) < sum): 
                l += 1
            else: 
                r -= 1
  
    return False
  
# Main Loop
if __name__ == '__main__':

    with open("input.txt") as file:
        input_dic = [l.rstrip("\n") for l in file]

        # Sort for efficiency
        input_dic.sort()

        # PART ONE
        find2Numbers(input_dic, 2020)

        # PART TWO
        arr_size = len(input_dic) 
        find3Numbers(input_dic, arr_size, 2020) 
