import sys
import socket
import select
import subprocess
 
def chat_client():
    if(len(sys.argv) < 3) :
        print 'Usage : python chat_client.py hostname port'
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])
    username = sys.argv[3]
    flag = 0
    flag2 = 0
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
     
    # connect to remote host
    try :
        s.connect((host, port))
    except :
        print 'Unable to connect'
        sys.exit()
     
    print 'Connected to remote host. You can start sending messages'
    sys.stdout.write('['+username+']'); sys.stdout.flush()
     
    while 1:
        socket_list = [sys.stdin, s]
         
        # Get the list sockets which are readable
        ready_to_read,ready_to_write,in_error = select.select(socket_list , [], [])
        
        for sock in ready_to_read:             
            if sock == s:
                # incoming message from remote server, s
                data = sock.recv(4096)
                print data
                if not data :
                    print '\nDisconnected from chat server'
                    sys.exit()
                else :
                    # print flag2
                    if flag2 == 0:
                        hasilkey = (msg**int(data))%q
                        sys.stdout.write(hasilkey)
                        sys.stdout.write('['+username+']'); sys.stdout.flush()
                        flag2 = 1
                    else:
                        # print 'flag didalem else %d' % flag2
                        source = data.split(':')[0]
                        encryptedmsg = data.split(':')[1].split('\n')[0].strip()
                        # print encryptedmsg
                        # print 'this is message that send from the server : %s' % encryptedmsg
                        sharedkey2 = int(data.split('\n')[1])
                        clientComputes = (sharedkey2**xvalue)%q
                        # print "this is the value that client computes: %s" % clientComputes
                        # print sharedkey2
                        # print source
                        # print encryptedmsg
                        cmd = ["python", "decrypt-des.py", "%s" %encryptedmsg]
                        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
                        # for line in proc.stdout.readlines():
                        #     print line
                        decryptedmsg = proc.stdout.readlines()[2]
                        # print decryptedmsg
                        # print decryptedmsg
                        # sys.stdout.write(source+decryptedmsg)
                        sys.stdout.write('\n'+source+decryptedmsg) 
                        # sys.stdout.write(data)
                        sys.stdout.write('['+username+']'); sys.stdout.flush()     
            
            else :
                # print flag
                if flag == 0:
                    #-------------------diffie-hellman starts here--------------------------------
                    q=17 # publicly known must be prime
                    a=3 # publicly known
                     
                    msgraw = sys.stdin.readline().strip()
                    msg = int(msgraw)
                    sharedkey = str((a**msg)%q)
                    s.send(sharedkey)
                    sys.stdout.write('['+username+']'); sys.stdout.flush()
                    flag = 1
                else:
                    # user entered a message
                    msg = sys.stdin.readline().strip()
                    # print 'tailahtaikucing'
                    # print msg
                    cmd = ["python", "des.py", "%s" %msg]
                    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
                    # for line in proc.stdout.readlines():
                    #     print line
                    encryptedmsg = proc.stdout.readlines()[2]
                    s.send(encryptedmsg+username)
                    print encryptedmsg
                    sys.stdout.write('['+username+']'); sys.stdout.flush() 

if __name__ == "__main__":

    sys.exit(chat_client())