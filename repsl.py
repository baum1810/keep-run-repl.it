from os import system
import threading

threads = int(input("how many links: "))
def main():
    name = input("projekt name: ")
    user = input("username: ")
    print("running")
    while True:
        system(f"curl -m 100 https://{name}.{user}.repl.co/ >NUL")
for i in range(threads):
    threading.Thread(target=main).start()