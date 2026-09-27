import time
from datetime import datetime
from zoneinfo import ZoneInfo
import zoneinfo

now = datetime.now(ZoneInfo("Asia/Karachi"))

print("Current local time :" , now.strftime("%y-%m-%d %h:%M:%S %Z%z"))

epc = time.time()
print(epc)
localtime = time.localtime(epc)

print("Local current time :", time.asctime(localtime))