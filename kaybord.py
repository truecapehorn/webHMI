# import time
# from threading import Thread
#
# answer = None
# t = 5  # You can type for 5 seconds
#
# def check():
#     time.sleep(5)
#     if answer != None:
#         print('ok wykonuj program 1',answer)
#         return
#     print("Too Slow")
#
# Thread(target=check).start()
#
# answer = input("Input something: ")



# from datetime import datetime, timedelta
# answer = None
# t = 5  # You can type for 5 seconds
# def timeup():
#     final_time = datetime.now() + timedelta(seconds=t)
#     print("You can enter now for" + str(t) + " seconds")
#     while datetime.now() < final_time:
#         print(datetime.now())
#         answer = input()
#         if datetime.now() > final_time:
#             if answer != None:
#                 print('ok wykonuj program 1',answer)
#                 break
#             else:
#                 print('dupa')
#                 break
#
#
#     print("STOP TYPING")
#
# timeup()
#
#
from threading import Timer
import sys
import time

def printer(s):
    print(s)
    for i in range(1,10):
        print(i)
        time.sleep(0.3)
    sys.exit()

timeout = 5

t = Timer(timeout, printer, ['Czas mnią i wykonuje sie program drugi'])
t.start()
prompt = "You have %d seconds to choose the correct answer...\n" % timeout


answer = input(prompt)
print(answer)
t.cancel()

