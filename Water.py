 from plyer import notification
 import time

 REPEAT_INTERVAL = 10

 notification.notify(
 title = "Go drink some water Krishna",
 message = "This is a sample notification",
 timeout = 10
 )
 time.sleep(REPEAT_INTERVAL)
