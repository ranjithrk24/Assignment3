def count():
    string=input('Sample String')
    upper_case=0
    lower_case=0
    for i in string:
        if ord(i)>=ord('A') and ord(i)<=ord('Z'):
            upper_case+=1
        elif ord(i)>=ord('a') and ord(i)<=ord('z'):
            lower_case+=1
    return upper_case,lower_case
a=count()
print('No. of Upper case characters:',a[0])
print('No. of Lower case characters:',a[1])
