file1 = open('exam-data/English.txt', 'r')
Lines = file1.readlines()

# Strips the newline character
for line in Lines:
    if line.startswith("25"):
        line = line.replace("25", " ")
        print("savol: ", line.strip())
    if line.startswith("A."):
        line = line.replace("A.", " ")
        print("A:", line.strip())
    if line.startswith("B."):
        line = line.replace("B.", " ")
        print("B:", line.strip())
    if line.startswith("C."):
        line = line.replace("C.", " ")
        print("C:", line.strip())
    if line.startswith("D."):
        line = line.replace("D.", " ")
        print("D:", line.strip())
    
    # print("Line {}: {}".format(count, line.strip()))