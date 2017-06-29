from spy_details import spy,Spy,ChatMessage,friends
from new import average
from datetime import datetime
from steganography.steganography import Steganography
from colorama import init,Fore,Style,Back




#-------------CREATE NEW USER---------------

def add_Friend():

    spy.name = raw_input("Enter your friend name: ")
    while spy.name.isalpha() == False:
        spy.name = raw_input("Name contains only'A-Z' or 'a-z' alphabets.Please enter again: ")

    spy.salutation = raw_input("Which one would you prefer for your friend \" Mr or Ms. \" :")
    value = True
    while value :
        if spy.salutation == 'mr' or spy.salutation == 'Mr' or spy.salutation == 'MR' or spy.salutation =='ms' or spy.salutation == 'Ms' or spy.salutation == 'MS' :
            value =False
        else :
            spy.salutation = raw_input("Please enter a valid salutation \" Mr or Ms. \": ")

    spy.salutation = 'M' + spy.salutation[1:]
    while len(spy.name) <= 0:
        spy.name = raw_input("Please enter valid name: ")

        spy.name = spy.salutation + " " + spy.name
        print("Welcome " + spy.name)
    spy.name = spy.salutation + " " + spy.name

    confirmAge = raw_input("Hey dude your is in B/W (12 - 50) years ? if yes then press'Y',if not then press any other: ")
    if confirmAge.upper() != 'Y':
        print("Sorry ! You can't become a spy.")
        exit()
    else:
        spy.age = int(raw_input("Enter your friend age: "))
        while spy.age > 50 or spy.age < 12:
            spy.age = int(raw_input("Incorrect Age. Please enter again: "))

        spy.rating = float(raw_input("Enter your friend rating: "))
        while spy.rating < 0 or spy.rating > 5:
            spy.rating = float(raw_input("Incorrect Rating. Please enter again: "))

        spyIsOnline = True
        friends.append(spy)
        print("Now your friend '"+spy.salutation+" "+spy.name+"' is online..")
        # --------TOTAL NO OF FRIENDS-------------#
        total_Friends = len(friends)

        print("Total number of friends you have = "+str(total_Friends))


#-----------------------STARTING OF CHAT APPLICATION---------------------------------------#

print("-------------------WELCOME TO SPY-CHAT-------------------")
existing = raw_input("Do You Want To Continue As  "+spy.salutation+" "+spy.name+"  OR create a new user ('Y'/'Press any key')?:")
if existing.upper() == "Y" :
    print("Welcome--"+spy.salutation+spy.name+"\n"+"         Age: "+str(spy.age)+"\n"+"         Rating: "+str(spy.rating)+"\n     "+"\"***Proud to have you with us***\"")
else :
    print ("--------------First you have to full-fill the requirements-----------")
    spy.name = raw_input("Enter your name: ")
    while spy.name.isalpha() == False:
        spy.name = raw_input("Name contains only'A-Z' or 'a-z' alphabets.Please enter again: ")

    spy.salutation = raw_input("Which one would you prefer Mr or Ms. :")
    spy.salutation = 'M' + spy.salutation[1:]
    while len(spy.name) <= 0:
        spy.name = raw_input("Please enter valid name: ")

        spy.name = spy.salutation + " " + spy.name
        print("Welcome " + spy.name)
    spy.name = spy.salutation + " " + spy.name

    confirmAge = raw_input("Hey dude are you in B/W (12 - 50) years ? if yes then press'Y',if not then press any other: ")
    if confirmAge.upper() != 'Y':
        print("Sorry ! You can't become a spy.")
        exit()
    else:
        spy.age = int(raw_input("Enter your age: "))
        while spy.age > 50 or spy.age < 12:
            spy.age = int(raw_input("Incorrect Age. Please enter again: "))

        spy.rating = float(raw_input("Enter your rating: "))
        while spy.rating < 0 or spy.rating > 5:
            spy.rating = float(raw_input("Incorrect Rating. Please enter again: "))

        spyIsOnline = True

        print("Welcome--" + spy.salutation + spy.name + "\n" + "         Age: " + str(
            spy.age) + "\n" + "         Rating: " + str(spy.rating) + "\n     " + "\"***Proud to have you with us***\"")



avail_Status = ['ON MISSION','YOU WILL NEVER GUESS MY SECRETS',"I'M INVINCINBLE"]

def add_Status():
    print("Your current status : "+str(spy.current_status_message))
    print("Do you wanna update your status OR not ?.")
    choice = raw_input("Press 1 to use old statuses or any other key to add a new one: ")

    if choice.isdigit() == 1 :
        count = 1
        for temp in avail_Status :
            print(str(count)+". "+temp)
            count = count + 1
        choose = int(raw_input("Choose your status: "))
        current_Status = avail_Status[choose - 1]
        print("Your new status-------:"+"\" "+current_Status+" \"")
    else :
        new_Status = raw_input("Please enter a new status: ")
        current_Status = new_Status
        print("You new status -------:"+"\" "+current_Status+" \"")
        avail_Status.append(current_Status)




#-------------------------------------SELECT A FRIEND()-----------------------------------------#
def select_a_Friend() :
    print("--------LIST OF YOUR FRIENDS--------")
    count = 1
    for temp in friends :
        print(str(count)+". "+temp.salutation+" "+temp.name)
        count +=1

    totalFriends = len(friends)
    select = int(raw_input("Select a friend: "))
    while select > totalFriends  or select <= 0:
        select = int(raw_input("No such type of friend lie at this position in your friend list.Please enter again:"))

    return (select - 1)

#-----------------------------SEND_A_SECRETMESSAGE()---------------------------------------------#


def send_a_secretMessage() :
    select = select_a_Friend()
    receiver = select
    #org_Img = raw_input("Please enter the name of the image:  ")
    org_Img = "C:\Users\Lakshay Rajput\PycharmProjects\untitled\\z.jpg"
    new_Img = raw_input("New name of the image: ")
    new_Img = "C:\Users\Lakshay Rajput\PycharmProjects\untitled\\" +new_Img+".jpg"
    text = raw_input("Enter the message you wanna send to your friend: ")
    while len(text) <=0  :
        text = raw_input("You didn't send any message.PLzz enter again: ")

    Steganography.encode(org_Img,new_Img,text)
    chat = ChatMessage(text, True)
    friends[select].chats.append(chat)

    print (friends[select].chats[0].message)

#send_a_secretMessage()
    #print("-----------Finally you have sent message to your friend---------")
    #print("\" " + friends[receiver].salutation + friends[
     #   receiver].name + " \" You got a new message--------:\"" + text + "\"")



receiver = 0

x = 0

def read_message() :


        sender = select_a_Friend()
        receiver = sender
        output_path = raw_input("What is the name of the file?")
        output_path = "C:\Users\Lakshay Rajput\PycharmProjects\untitled\\" +output_path+".jpg"
        secret_text = Steganography.decode(output_path)
        #var = "The message is empty...."
        if secret_text == 'SOS':
            txt = "I'm on the way,just send me your location"
            print(txt)
            new_chat = ChatMessage(txt, False)
            spy.chats.append(new_chat)
            print(spy.chats[0].message)
        elif secret_text == 'SM':
            txt = "I'm coming to save you.."
            print(txt)
            new_chat = ChatMessage()
            spy.chats.append(new_chat)
            print(spy.chats[0].message)
        elif secret_text == 'FITH':
            txt = "Fire in the hole"
            print(txt)
            new_chat = ChatMessage(txt, False)
            spy.chats.append(new_chat)
            print(spy.chats[0].message)
        elif secret_text == 'CM':
            txt = "Provide him protection"
            print(txt)
            new_chat = ChatMessage(txt, False)
            spy.chats.append(new_chat)
            print(spy.chats[0].message)
        else:
            newchat = ChatMessage(secret_text, False)
            friends[sender].chats.append(newchat)

        print "Your secret message has been saved!"

        main= average(secret_text)
        x = len(secret_text.split())

        if x>=100 :
            print("Before deleting the friend , you had "+str(len(friends)))
            del friends[sender]
            print("After deleting you have "+str(len(friends))+" friends")










#---------------------------Check Chat History-----------------------------------



def chatHistory():
    read_for = select_a_Friend()

    print("You have selected-------:\" "+friends[read_for].salutation+friends[read_for].name+" \"who's chat history you wanna read------")

    init(autoreset=True)
    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            
            print("[%s] [%s] , %s %s: %s" % (chat.time.strftime("%d %B %Y"), Fore.BLUE + chat.time.strftime(" %H:%M:%S"), Fore.RED + spy.name ,Fore.BLACK + "said : ",chat.message))
           # print ("[%s] %s %s: %s" % (chat.time.strftime("%d %B %Y"),    Fore.GREEN + spy.name              ,    Fore.BLACK + 'said:',   chat.message))
        else:
            print("[%s] [%s] , %s %s: %s" % (
            chat.time.strftime("%d %B %Y"), Fore.BLUE + chat.time.strftime(" %H:%M:%S"), Fore.RED + friends[read_for].name,
            Fore.BLACK + "said : ", chat.message))

            #print ("[%s] %s %s: %s" % (chat.time.strftime("%d %B %Y"),    Fore.GREEN + friends[read_for].name,    Fore.BLACK + 'said:',   chat.message))
    init(autoreset=False)





#----------------------LETS START THE CHAT--------------------------#

def startChat() :
    menu = True
    while menu :
        print("What do you wanna do ?.")
        print(" 1. **Add a status**.....\n 2. **Add a friend**....\n 3. **Send a secret message**....\n 4. **Read a secret message**....\n"
              " 5. **Read chats from a user**....\n 6. **Close the Application**....\n")
        choice = int(raw_input("Enter your choice: "))
        while choice <= 0 or choice > 6 :
            choice = int(raw_input("Please enter a digit B/W '1-6': "))

        if choice == 1 :
            add_Status()
        elif choice == 2 :
            add_Friend()
        elif choice == 3 :
            send_a_secretMessage()
        elif choice == 4 :
            read_message()
        elif choice == 5 :
            chatHistory()
        elif choice == 6 :
            menu = False

    exit()


startChat()
