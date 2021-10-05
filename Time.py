class Time:
  def __init__(self, h, m, s):
    self.hours = h
    self.minutes = m
    self.seconds = s

  def getHours(self):
    return self.hours
  def getMinutes(self):
    return self.minutes
  def getSeconds(self):
    return self.seconds

  #toString
  #This method returns a String in the format of hour:minute:second
  #@return String: returns the fields in a formatted String
  def toString(self):
    s = "{}:{}:{}"
    return s.format(self.hours, self.minutes, self.seconds)

  #timeInSeconds
  #This method converts the Time object into an int of seconds
  #@return int: Returns the fields all converted into seconds
  def timeInSeconds(self):
    return self.hours * 60 * 60 + self.minutes * 60 + self.seconds

  # changeTheTime
  # This method will move replace the current time with another time
  # Precondition: All parameters are within normal ranges for hours, minutes, and seconds
  # @param h: This is the number of hours
  # @param m: This is the number of minutes
  # @param s: This is the number of seconds
  def changeTheTime(self, h, m, s):
    self.hours = h
    self.minutes = m
    self.seconds = s

  # twelveHourClock
  # This method will return as a String, the Time object with an am or pm reference
  # @return String: This will be the time, but converted to the am or pm version of the time
  def twelveHourClock(self):
    if self.hours <= 12:#if the hours of the time that called the method is less than 12
      return self.toString() + " am"
    else:
      newTime = Time(self.hours - 12, self.minutes, self.seconds)
      return newTime.toString() + " pm"

  # whatTimeIsIt
  # Based on the time, return morning, afternoon, evening, or nighttime
  # @return String: if time is between 6-12, return morning;if time is between 12 - 5 return afternoon;
  # if time is between 5 - 10 return evening;if time is between 10 - 6 return nighttime
  def whatTimeIsIt(self):
    if self.hours >= 6 and self.hours < 12:#if hours is between 6 and 12
      return "morning"
    elif self.hours >= 12 and self.hours < 17:#if hours is between 12 and 17
      return "afternoon"
    elif self.hours >= 17 and self.hours < 22:#if hours is between 17 and 22
      return "evening"
    else:#if hours is 22 to 24 or 0 to 6
      return "nighttime"

  # compareTo
  # This method compares the Time object that called the method to the Time object parameter
  # The difference between the two times should be the number of seconds between the two time objects
  # @param t: This is a Time object
  # @return int: negative means the object that called the method is before the parameter
  # positive means the object that called the method is after the parameter
  # zero means the object and the parameter are the same time
  def compareTo(self, t):
    return self.timeInSeconds() - t.timeInSeconds()

  # timeTill
  # This method returns a Time object representing how long from the current time to the parameter Time
  # @parameter t: This Time object represents a time in the future
  # @return Time: returns a Time object that represents how long till the Time parameter
  def timeTill(self, t):
    secDif = t.compareTo(self)
    h = secDif // 3600
    secDif -= h * 3600
    m = secDif // 60
    s = secDif - m * 60
    return Time(h,m,s)