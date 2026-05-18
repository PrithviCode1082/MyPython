# Playlist Manager
# Build a music playlist using a list. 
# Support: add song, remove song, shuffle, display all (numbered), and search by name.
import random

songs = ["New World Order", "Butterflies", "Meadows", "Mochis"]

def displaySongs():
    for i in range(0, len(songs)):
        print(f"{i+1} - {songs[i]}")

def menu():
    print("***** MENU *****")
    print("1. Play a Song\n2. Move Next\n3. Move previous\n4. Add Song\n5. Remove Song\n6. Display All\n7. Shuffle")

# menu()
choice = 1
num = -1

while (choice != 0):
    menu()
    choice = int(input("Enter a choice: "))
    match(choice):
        case 1:
            displaySongs()
            num = int(input("Enter the song number to play: ")) - 1
            print(f"{songs[num]} is playing!")
        case 2:
            if num == -1:
                print("Select a Song to start playing")
            else:
                if num == len(songs) - 1:
                    num = -1
                print(f"{songs[num+1]} is playing!")
                num += 1
        case 3:
            if num == -1:
                print("Select a Song to start playing")
            else:
                if num == 0:
                    num = len(songs)
                print(f"{songs[num-1]} is playing!")
                num -= 1
        case 4:
            songName = input("Enter the song's name: ")
            songs.append(songName)
            print(f"{songName} was added to list!")
        case 5:
            displaySongs()
            rem = int(input("Enter the number of the song to remove: "))
            del songs[rem-1]
        case 6:
            displaySongs()
        case 7:
            random.shuffle(songs)
        case _:
            break
