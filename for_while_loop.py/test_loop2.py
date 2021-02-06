# 2.จงเขียนตารางสูตรคูณให้ผลลัพท์ที่ออกมาเป็นแบบตัวอย่างด้านล่างโดยใช้คำสั่ง for
for multitable in range(2, 13):
    print("   [{}]".format(multitable))
    for value in range(1, 13):
        print("{} * {} : {}".format(multitable, value, value * multitable))
print("-----------------")