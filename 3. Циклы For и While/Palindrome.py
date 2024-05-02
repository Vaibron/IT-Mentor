tmp = '1a1a1'
def pal(a):
    start, end = 0, len(tmp)-1
    while start != end:
        if not a[start].isalpha():
            start += 1
        elif not a[end].isalpha():
            end -= 1
        elif a[start].lower() == a[end].lower():
            start += 1
            end -= 1
        else:
            return False

    return True

print(pal(tmp))