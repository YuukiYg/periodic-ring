import playsound
import sys
import time
import threading

def ring():
    playsound.playsound('ring.mp3')

if __name__ == '__main__':
    args = sys.argv
    if 2 <= len(args):
        if not args[1].isdigit():
            print('Argument must be an integer: ' + args[1])
            sys.exit()
    else:
        print('Usage: python ring.py second')
        print('  Ex) python ring.py 10')
        sys.exit()

    period = args[1]
    print('Ring every ' + period + ' seconds. [Ctrl + C to stop]')
    while True:
        threading.Thread(target=ring).start()
        time.sleep(int(period))
