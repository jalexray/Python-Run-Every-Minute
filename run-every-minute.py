import datetime
import time

now = datetime.datetime.now()
old_now = now

while 1:
	now = datetime.datetime.now()
	if(int(now.minute) - int(old_now.minute) != 0):
		print("I am gonna run a cool function")
		old_now = now
		time.sleep(20)
	else:
		print("I already ran a cool function this minute.")
		time.sleep(20)
