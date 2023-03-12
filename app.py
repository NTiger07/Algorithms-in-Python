# print("Que miras bobo")

def permuteRecur(string, pocket=""):
    if len(string) == 0:
        print(pocket)
    else:
        for i in range(len(string)):
            letter = string[i]
            head = string[0:i]
            tail = string[i+1:]
            together = head + tail
            permuteRecur(together, letter + pocket)
        # print(len(permuteRecur))
            
permuteRecur("ABCD", "")
            
            