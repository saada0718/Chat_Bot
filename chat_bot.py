from pynput.keyboard import Key, Controller
import webbrowser
import requests
from bs4 import BeautifulSoup
class Node:
    def __init__(self,left=None,right=None,parent=None,data=None,info = None,num = None):
        self.parent = parent
        self.right = right
        self.left = left
        self.data = data
        self.info = info
        self.num = 0

    def common(self):
        self.num+=1


class InternetNode:
    def __init__(self,left=None,right=None,parent=None,data=None,url=None):
        self.parent = parent
        self.right = right
        self.left = left
        self.url = url
        self.data = data

adam = Node(None,None,None,None,None,0)
internet_adam = InternetNode(None,None,None,None,None)
def find_node(final,person):
    check = final
    while not(check == None) and not(check.data == person) and not(check.data == None):
        if check.data < person:
            if check.right == None:
                break
            check = check.right
        elif check.data > person:
            if check.left == None:
                break
            check = check.left
        elif check.data == person:
            break
    return check
"""
Put both of these functions in a try just in case the internet is not
connected
"""
def google(search):
    webbrowser.open('https://www.google.com/search?q='+search)
    keyboard = Controller()
    key = '\n'
    keyboard.press(key)
    keyboard.release(key)


def _go_to_helper(search):
    soup = BeautifulSoup(requests.get('https://www.google.com/search?q=' + search).text, features="lxml")
    count = 0
    for link in soup.find_all('a'):
        if 'https://www.' in link.get('href'):
            send_link = ""
            testing = False
            slash = 0
            for i in range(len(link.get('href'))):
                if link.get('href')[i] == '/':
                    slash += 1
                if slash == 4:
                    break
                if link.get('href')[i] == 'h':
                    testing = True
                if testing:
                    send_link += link.get('href')[i]
            webbrowser.open(send_link)
            break
    correct = input("Was this the right website? If no then type in \"no\" otherwise just press enter ")
    if correct.lower() == "no":
        correct_url = input("Please enter the correct url for next time ")
        if internet_adam.data == None:
            internet_adam.data = search
            internet_adam.url = correct_url
        else:
            temp = internet_adam
            temp = find_node(internet_adam, search)
            if temp.data < search:
                temp.right = InternetNode(None, None, temp, search, correct_url)
            elif temp.data > search:
                temp.left = InternetNode(None, None, temp, search, correct_url)
def go_to(search):
    temp = internet_adam

    temp =  find_node(temp,search)
    if temp!=None:
            if temp.data == search:
                webbrowser.open(temp.url)
            else:
                _go_to_helper(search)
    else:
       _go_to_helper(search)
while True:
    person = input("Please type in what you would like to say to the chat bot (Type \"quit\" to quit): \n")
    if person[:6].lower() == "search":
        try:
            google(person[7:])
        except:
            print("An error occured.")
    elif person[:5].lower() == "go to":
        try:
            go_to(person[5:])
        except:
            print("A problem occurred try checking if the internet is connected or something.")
    else:
        if person == "quit":
            break
        elif person == "":
            print("You did not enter anything. Please try again.")
            continue
        check = find_node(adam,person)
        if check.data == None:
            check.data = person
            print("I have never heard of this word can you please tell me how a person would respond to this?")
            temp = None
            while True:
                ask = input("Response (Enter \"-1\" to exit): ")
                if ask == "-1":
                    break
                if check.info == None:
                    check.info = Node(None,None,None,ask,None,0)
                    temp = check.info
                else:
                    temp.info = Node(None,None,None,ask,None,0)
                    temp = temp.info
            if check.info != None:
                print(check.info.data)

        elif check.data!=person:
            if check.data > person:
                check.left = Node(None,None,None,None,0)
                check.left.data = person
                check.left.parent: check
                check.left.info = None
                temps = None
                while True:
                    ask = input("Response (Enter \"-1\" to exit): ")
                    if ask == "-1":
                        break
                    if check.left.info == None:
                        check.left.info = Node(None, None, None, ask, None, 0)
                        temps = check.left.info
                    else:
                        temps.info = Node(None, None, None, ask, None, 0)
                        temps = temps.info
                if check.left != None:
                    if check.left.info!=None:
                        print(check.left.info.data)
            elif check.data < person:
                check.right = Node(None,None,None,None,0)
                check.right.data = person
                check.right.parent: check
                check.right.info = None
                tempy = None
                while True:
                    ask = input("Response (Enter \"-1\" to exit): ")
                    if ask == "-1":
                        break
                    if check.right.info == None:
                        check.right.info = Node(None, None, None, ask, None, 0)
                        tempy = check.right.info
                    else:
                        tempy.info = Node(None, None, None, ask, None, 0)
                        tempy = tempy.info
                if check.right!= None:
                    if check.right.info!=None:
                        print(check.right.info.data)
        elif check.data == person:
            check.common()
            first_adam = adam
            temporary = check.info
            Store = temporary
            while not(temporary == None) and not(temporary.data == None):
                first_adam = find_node(first_adam,temporary.data)
                if first_adam.num > Store.num:
                    Store = first_adam
                first_adam = adam
                temporary = temporary.info
            if Store != None:
                if Store.data != None:
                    print(Store.data)
