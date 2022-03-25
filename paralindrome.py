def isPalindrome(ar):
    for i in range(0, int(len(ar)/2)):
        if ar[i] != ar[len(ar)-i-1]:
            return False
    return True
def countVowel(ar):
    ac= 0
    ec= 0
    jc= 0
    oc= 0
    uc= 0
    for i in range(len(ar)-1):
        if ar[i] == "a":
            ac+= 1;
            print("Pos a is :",i+1)
        elif ar[i] == "e":
            ec +=1;
            print("Pos e is :",i+1)
        elif ar[i] == "i":
            jc +=1;
            print("Pos i is :",i+1)
        elif ar[i] == "o":
            oc +=1;
            print("Pos o is :",i+1)
        elif ar[i] == "u":
            uc +=1;
            print("Pos u is :",i+1)
    print("The word:", ar," has:  a , e , i , o , u ",ac," ",ec," ",jc," ",oc," ",uc)
    #s = "The word:"+ ar+" has:  a , e , i , o , u "+ac+" "+ec+" "+jc+" "+oc+" "+uc
 
           
def main():
    #print("Enter palindrome word")
    #List = ["parap", "Fos", "wow"]
    #y = True
    readFile("para.txt")
 
    #for i in List:
    #    y = isPalindrome(i)
    #    if (y):
    #        print("Yes")
    #    else:
    #        print("No")
    #    countVowel(i)

def readFile(namefile):
    file1 = open(namefile, 'r')
    txt = file1.read()
    x = txt.split()
    for i in x:
        y = isPalindrome(i)
        if (y):
            print("Yes")
        else:
            print("No")
        countVowel(i)
    file1.close()
if __name__ == "__main__":
    main()
