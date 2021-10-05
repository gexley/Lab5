from Time import Time

time1 = Time(1,48,20)
time2 = Time(9,55,8)
time3 = Time(14,36,18)
time4 = Time(19,22,58)

print(time1.toString())
print(time2.toString())
print(time3.toString())
print(time4.toString())
print("\n")

print("time1 in seconds is:",time1.timeInSeconds())
print("time2 in seconds is:",time2.timeInSeconds())
print("time3 in seconds is:",time3.timeInSeconds())
print("time4 in seconds is:",time4.timeInSeconds())
print("\n")

time1.changeTheTime(23,9,49)
print("time1 is now:", time1.toString())
print("\n")

print(time2.twelveHourClock())
print(time4.twelveHourClock())
print("\n")

print(time1.whatTimeIsIt())
print(time2.whatTimeIsIt())
print(time3.whatTimeIsIt())
print(time4.whatTimeIsIt())
print("\n")

print("Time1 compared to Time2 =", time1.compareTo(time2))
print("Time3 compared to Time2 =", time3.compareTo(time2))
print("Time4 compared to Time1 =", time4.compareTo(time1))
print("Time1 compared to Time1 =", time1.compareTo(time1))
print("\n")

print("from Time2 till Time3 is", time2.timeTill(time3).toString())