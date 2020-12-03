# Day 3

def runTheMaze(maze, right_slope, down_slope):
     #for i in maze:
     #    print(i)
     trees = 0
     linecount = 0
     right = right_slope
     down = down_slope

     for line in maze:
         try:
             string = maze[down]
             string = string * 100

             char = string[right]

             if char != '.' :
                 trees += 1

             right += right_slope
             down += down_slope
             linecount += 1

         except:
             print("End of maze hit")
             break

     return trees

def file_len(name):
    for i, l in enumerate(name):
        pass
    return i + 1

# Main Loop
if __name__ == '__main__':

    counter = 0

    #Read input into list line by line
    with open("input.txt") as file:
        maze = [l.rstrip("\n") for l in file]

        print("PART ONE")

        # Get length of maze
        count = file_len(maze)
        print("Lines in maze:       ", count)

        # PART ONE
        count_of_trees = runTheMaze(maze, 3, 1)
        print("Number of trees hit: ", count_of_trees, "\n")

        # PART TWO
        print("PART TWO")
        one_count_of_trees = runTheMaze(maze, 1, 1)
        print("One Number of trees hit: ", one_count_of_trees, "\n")
        two_count_of_trees = runTheMaze(maze, 3, 1)
        print("Two Number of trees hit: ", two_count_of_trees, "\n")
        three_count_of_trees = runTheMaze(maze, 5, 1)
        print("Thr Number of trees hit: ", three_count_of_trees, "\n")
        four_count_of_trees = runTheMaze(maze, 7, 1)
        print("Fou Number of trees hit: ", four_count_of_trees, "\n")
        five_count_of_trees = runTheMaze(maze, 1, 2)
        print("Fiv Number of trees hit: ", five_count_of_trees, "\n")

        partTwoSolution = (one_count_of_trees * two_count_of_trees * three_count_of_trees * four_count_of_trees * five_count_of_trees)

        print("Part Two Solution:", partTwoSolution)
