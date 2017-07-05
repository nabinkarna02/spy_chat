from spy_details import spy, Spy, chat, friends #transferring data from spy_details file to main
from steganography.steganography import Steganography #To hide information in plain sight
from datetime import datetime
default_status = ["Hello! friends what's up","what a cool weather","Hanging out with music","what a busy day!"]#they are the default statuses or previous updated statuses
print "Hello! Let's explore :)"
spy_continue = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
#if user types y , below if statement will execute
#if user types n, below else statement will execute
SC = raw_input(spy_continue)
def status_update():#defining status_update
    current_status = None#displays current status
    if spy.current_status_message != None:
        print "Your current status is:\n" + spy.current_status_message
    else:
        print "Your status is empty :( \n"
    older_select = raw_input("Do you want to select from your previous statuses? (Y\N) ")
    if older_select.upper() == "N":#if user types N,it means user should type new status
        new_status = raw_input("Please type your new status.....")
        if len(new_status) > 0:
            default_status.append(new_status)
            current_status = new_status#status will be stored as current status
    elif older_select.upper() == 'Y':#if user types Y,it means user will select from previously stored statuses
        item_position = 1
        for message in default_status:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1#position is incremented i.e current typed status will be stored
        message_selection = int(raw_input("\nPlease select from above"))
        if len(default_status) >= message_selection:
            current_status = default_status[message_selection - 1]
    else:
        print "Invalid Input :(" #error if user types other than y or n
    if current_status:
        print "Your current status is " + current_status
    else:
        print "You current status is empty"
    return current_status#the current_status value is returned
def add_new_friend():#defining add_new_friend
    new_friend = Spy('','',0,0.0)
    print"Please fill the details below:"
    new_friend.name = raw_input("New friend name: ")
    new_friend.salutation = raw_input("Mr. or Ms.?: ")
    new_friend.name = new_friend.salutation + " " + new_friend.name
    new_friend.age = raw_input("Age:")
    new_friend.age = int(new_friend.age)
    new_friend.rating = raw_input("Spy rating:")
    new_friend.rating = float(new_friend.rating)#details of new friend
    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)#storing the info. of new friend
        print 'congratulations! Friend Added!'
    else:
        print "Sorry!your friend's details doesn't fulfil our requirements"
    return len(friends)#returning lenth of added friend to increment/count no. of friends
def friend_selection():#defining friend_selection
    item_number = 0
    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number +1, friend.salutation, friend.name,friend.age,friend.rating)
        item_number = item_number + 1
    choose_friend = raw_input("select your friend")
    friend_choice_position = int(choose_friend) - 1
    return friend_choice_position
def send_message():#defining send_message.used to send secret message
    choose_friend = friend_selection()
    original_image = raw_input("please type image name:")
    output_path = "output.jpg"
    text = raw_input("Type the text to hide ")
    Steganography.encode(original_image, output_path, text)#to hide text ,encode is done
    new_chat = chat(text,True)
    friends[choose_friend].chats.append(new_chat)
    print "congratulations! You have successfully created a secret message and is ready to use!"
def read_message():#to read secret message
    sender = friend_selection()
    output_path = raw_input("Enter name of file:")
    secret_text = Steganography.decode(output_path)#decoding is done to access the text hidden in image
    new_chat = chat(secret_text,False)
    friends[sender].chats.append(new_chat)
    print "Your secret message is saved successfully!"
def chat_history():#to check message history
    read_for = friend_selection()
    print '\n'
    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.msg)
        else:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.msg)
def chat_begin(spy):
    spy.name = spy.salutation + " " + spy.name
    if spy.age>=18 and spy.age<=45:
        print "Welcome " + spy.name + " age: " \
              + str(spy.age) + " and rating of: " + str(spy.rating) + " :)"
        show_menu = True
        while show_menu:#while loop continues until show_menu=false
            menu_choices = "What do you want to do? \n 1. Update a status \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats \n 6. Exit \n"
            menu_choice = raw_input(menu_choices)
            if len(menu_choice) > 0:#len counts the length of text
                menu_choice = int(menu_choice)#converts str into int
                if menu_choice == 1:
                    spy.current_status_message = status_update()#executes status_update() defined earlier
                elif menu_choice == 2:
                    number_of_friends = add_new_friend()#moves and executes add_new_friend defined above
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    send_message()#executes send_message defined above
                elif menu_choice == 4:
                    read_message()#executes read_message defined above
                elif menu_choice == 5:
                    chat_history()#executes chat_history defined above
                else:
                    show_menu = False
                    #while loop terminates
    else:
        print "Sorry ! couldn't proceed \neither you have entered wrong input or your details doesn't fulfil our requirements"
if SC == "Y" or SC == "y":#for old spy_user
    username=raw_input("Enter your username:")
    password=raw_input("Enter your password:")
    if username == "nabinkarna02" and password == "nnnnn":#if else is used for username and password
     chat_begin(spy)
    else:
        print"Incorrect Username or Password"
        exit()
elif SC == "N" or SC == "n":#for new user
    spy = Spy('','',0,0.0)
    spy.name = raw_input("Welcome!\n Your Name: ")
    spy.salutation = raw_input("Are you Mr. or Ms.?: ")
    spy.age = raw_input("Your age:")
    spy.age = int(spy.age)
    spy.rating = raw_input("Your rating (out of 5):")
    spy.rating = float(spy.rating)
    chat_begin(spy)#details of new user
else:#else statement executes if the user input does not satisfy if and elif condition
    print"wrong input"
    exit()