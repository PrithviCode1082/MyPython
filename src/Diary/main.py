# Diary App
from datetime import datetime as dt

def getCurrentDateTime():
    cr = dt.now()
    hour = cr.hour if cr.hour<=12 else (cr.hour-12)
    return f"\n----- {cr.day}/{cr.month}/{cr.year} ** ENTRY ** {hour}:{cr.minute}:{cr.second} -----\n"

def writeDiary():
    entry = input("Start Writing:\n")
    with open('records.txt', 'a') as writer:
        writer.write(getCurrentDateTime())
        writer.write(f"{entry}\n")
        writer.write("-----------------------------------------\n\n")

def readDiary():
    with open('records.txt', 'r') as reader:
        entries = reader.read()
        if entries.strip() == "":
            print("The File is empty, write entries to List!")
        else:
            print(entries)

writeDiary()
readDiary()