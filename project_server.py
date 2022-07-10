import socket
import random

score=0
questions=[['Capital of Egypt','Cairo',0],
['Basketball Goat','Jordan',0],
['Nba champions of 2018','GSW',0],
['Nba titles won by Kobe Bryant','5',0],
['Highest score in a cricket ODI match','481',0],
['Most wickets taken in a ODI match by a bowler','8',0],
['Most runs scored by a player in a ODI match',264,0],
['Most runs scored by a player in a test match','400',0],
['Year of declaration of independence of INDIA','1947',0]]

#creating socket
def create_socket():
    try:
        global host
        global port
        global s
        port = 9999
        host = "127.0.0.1"
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error"+msg)

#binding the socket &listen
def binding_socket():
    try:
        global host
        global port
        global s
        print("Binding the Port "+str(port))
        
        s.bind((host,port))
        s.listen(5)

    except socket.error as msg:
        print("Binding error :"+ str(msg))
        binding_socket()        

#accept connections
def accept_connection():
    con,addr=s.accept()
    print("connection established to port :"+str(addr[1])+" IP :"+addr[0])
    prog(con,addr)
    con.close()

#functionality
def prog(con,addr):
    print("The game has started")
    global questions
    global score
    flag=0
    while True:
        if score >=3:
            msg="You won!! Game ended"
            con.send(str.encode(msg))
            print("Game ended ")
            break
        else:
            i=(random.randint(0,15))%9
            ques=questions[i][0]
            if flag!=0:
                while questions[i][2]==1:
                    i=(random.randint(0,100))%9
                    ques=questions[i][0]
            else:
                flag=1
                ques=questions[i][0]
            questions[i][2]=1
            con.send(str.encode(ques))
            ans=str(con.recv(1024),"utf-8")
            if ans==questions[i][1]:
                score+=1
                con.send(str.encode("Right answer!,score increases by 1"))
            else:
                con.send(str.encode("Wrong answer!"))

def main():
    create_socket()
    binding_socket()
    accept_connection()

main()