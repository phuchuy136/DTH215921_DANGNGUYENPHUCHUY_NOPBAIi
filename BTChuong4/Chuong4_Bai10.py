#vẽ hình dùng sleep 
'''
Viết chương trình vẽ hình vuông, hình tròn, hình tam giác với thời gian dừng giữa các hình là 2 giây.
'''
import time
import os
#các hình 
hinh1 = """
   *
   **
   ***
*******
***
**
*
"""

hinh2 = """
   *
   **
   * *
*******
* *
**
*
"""

hinh3 = """
   ****
   ***
   **  
   *
  ** 
 ***
****
"""

hinh4 = """
   ****
   * *
   ** 
   *  
  **
 * *
****
"""

ds_Hinh = [hinh1, hinh2, hinh3, hinh4]
print("==Chương trình vẽ hình==")
for hinh in ds_Hinh:
    os.system('cls') #dùng lệnh cls
    print(hinh)
    time.sleep(2) #dừng 2 giây