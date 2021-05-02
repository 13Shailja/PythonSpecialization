#%% Assignment 9.4

# ===============================================================================================================================
# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address 
# to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary 
# using a maximum loop to find the most prolific committer.
# ===============================================================================================================================

name = input("Enter file: ")
if len(name) < 1: name = "mbox-short.txt"

fileHandle = open(name)

senderCount = dict()

for line in fileHandle:
    if line.startswith('From '):
        words = line.split()
        sender = words[1]
        senderCount[sender] = senderCount.get(sender, 0) + 1
        
mostSender = None
mostCount = None

for sender, scount in senderCount.items():
    if mostCount is None or mostCount < scount :
        mostCount = scount
        mostSender = sender
        
print(mostSender, mostCount)
