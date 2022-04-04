
def sorti(lst):
    lsti.sort()
    print(lsti)

def desort(lst):
    lsti.sort(reverse=True)
    print(lsti)

ele = input("enter list input seperated by space: ")
lsti = list(map(int,ele.split()))
print(lsti)

sorti(lsti)
desort(lsti)