def(is leapyear(year):
if(year%4==0and year%100!=0)or
year%400==0:
  return true
else:
  return False
  year=2012
  if is leapyear(year):
    print("() is a leap year. ".format(year))
  else:
    print("()is not a leap year. ".format(year))