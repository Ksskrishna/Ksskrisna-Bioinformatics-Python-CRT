num = int(input("range of list: "))
songs=[]
for i in range(num):
    temp = input("enter the songs: ")
    songs.append(temp)
print(songs)

num2=int(input("enter how many you want to add: "))
new_songs=[]
for i in range(num2):
    temp = input("enter new songs: ")
    new_songs.append(temp)
songs.append(new_songs)
print(songs)
print(songs[::-1])