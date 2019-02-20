import time
from threading import Thread

answer = None
t = 5  # You can type for 5 seconds

def check():
    time.sleep(5)
    if answer != None:
        print('ok wykonuj program 1',answer)
        return
    print("Too Slow")

Thread(target=check).start()

answer = input("Input something: ")



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
#     print("STOP TYPING")
#
# timeup()

