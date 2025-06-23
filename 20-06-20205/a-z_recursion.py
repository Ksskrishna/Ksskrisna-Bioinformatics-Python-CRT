'''
write a python prog to print alphabets from a to z using recursion
'''

def alphabets(ch):
    if ch>=ord('A') and ch <= ord('Z'):
        print(chr(ch))
        return alphabets(ch+1)
ch = 65
alphabets(ch)
print("_________________________________")