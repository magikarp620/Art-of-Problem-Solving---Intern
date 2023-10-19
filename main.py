# Open the input file and read the content
with open('pyramid_sample_input.txt', 'r') as file:
    input_lines = file.readlines()

# Extract the target value from the first line by splitting the text
t = int(input_lines[0].split(':')[1].strip())

# Initialize an empty 2D array
matrix = []

# Iterate through the lines and split values to form the 2D array
for line in input_lines[1:]:
    row = list(map(int, line.strip().split(',')))
    matrix.append(row)
# Define Variables
rows = len(matrix)
#FindPath recursive function
def FindPath(r, c, target, path):
    #If the number cannout be devided to an integer it is not he path we want
    if target % matrix[r][c] != 0:
        return None
    
    if target == matrix[r][c]:
        return path
    
    if r == rows - 1:
        return None
    #Each number has two possible path
    left_path = FindPath(r + 1, c, target // matrix[r][c], path + 'L')
    right_path = FindPath(r + 1, c + 1, target // matrix[r][c], path + 'R')

    #Return logic
    if left_path:
        return left_path
    elif right_path:
        return right_path
    else:
        return None
#Write path to file
output_file = open("output.txt", "w")
output_file.write((FindPath(0,0, t, "")))
output_file.close()
