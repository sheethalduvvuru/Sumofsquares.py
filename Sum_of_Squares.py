def squaresum(counter,alist):
 if counter==0:
    return 0
 else:
    if int(alist[counter-1])<0:
        return 0 + squaresum(counter-1, alist)
    else:
        return int(alist[counter-1])**2 + squaresum(counter-1,alist)


def testcase(a):
    if a==0:
        return
    terms = int(input())
    nums = input()
    list1 = nums.split()
    print(squaresum(terms,list1))
    testcase(a-1)
    

if __name__=='__main__':
    casecount = int(input())
    testcase(casecount)
