import time
import os


x = 20
while x > 0:
    print(f"Бомба взорвётся через {x} секунд...")
    x -= 1
    time.sleep(1)
print("#"*10000)
time.sleep(1)
os.system("sudo shutdown -h now")
