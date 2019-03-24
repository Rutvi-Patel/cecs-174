
time1 = str((input("Enter the first time as hours:minutes in 24 hour format:")))
time2 = str((input("Enter the second time as hours:minutes in 24 hour format:")))
t1s = time1.split(":")
t2s = time2.split(":")
x, y = time1.replace(":", ""), time2.replace(":", "")
if ';' in time1 or ';' in time2:
    print("Invalid format!!!")
elif not x.isdigit():
    print("Invalid entry - input should be numbers only.")
elif not y.isdigit():
    print("Invalid entry - input should be numbers only.")
else:
    t1h, t1m = int(t1s[0]), int(t1s[1])
    t2h, t2m = int(t2s[0]), int(t2s[1])
    if (t1h >= 24) or (t2h >= 24) or (t1m >= 60) or (t2m >= 60):
        print("Invalid time range.")
    else:
        if t1h < t2h:
            print("time1 comes first")
        elif t1h == t2h:
            if t1m < t2m:
                print("time1 comes first")
            elif t1m == t2m:
                print("time1 and time2 are the same")
            else:
                print("time2 comes first")
        else:
            print("time2 comes first")

