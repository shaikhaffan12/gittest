def repeat(string,a):
    if a==0:
        return 1
    else:
        print(string)
        return repeat(string,a-1)

repeat('affan', 5)