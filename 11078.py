T = int(input())
students = []
diff_sinior = 0
sinior_exist = False

for case in range(T):
    n = int(input())
    for index in range(n):
        students.append(int(input()))
    j=0
    for i in range(n-1):        
        if students[j] > students[i+1]:
            sinior_exist = True
            temp = students[j] - students[i+1]                  
            if temp > diff_sinior:
                diff_sinior = temp
        else:
            j = i+1
    if not sinior_exist:
        diff_sinior = students[n-2] - students[n-1]
    sinior_exist = False
    print(diff_sinior)
    diff_sinior = 0
    students = []
    


