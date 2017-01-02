import time
import webbrowser


total_break=3
count=0

print("now the time is"+time.ctime())
while(count<total_break):
  time.sleep(2)
  webbrowser.open("www.baidu.com")
  count=count+1