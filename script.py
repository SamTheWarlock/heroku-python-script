print("© CheeseRespect2019 and Samuel B. Developments 2020")
print("For suggestions on what information this should include, DM SprlteCranberry#6049")
print("______________________________________")
print("______________________________________")
print()
while True:
  theiruser = input("Please enter username: ")
  from pyblox3 import Groups
  #"https://api.roblox.com/Users/get-by-username?username=" + theiruser
  import requests
  resp = requests.get('https://api.roblox.com/Users/get-by-username?username=' + theiruser)
  e = resp.content
  import json
  my_string = e.decode()
  my_list = json.loads(my_string)
  import requests
  try: 
    taa = requests.get('https://users.roblox.com/v1/users/' + str(my_list['Id']) + '/')
  except:
    print("User is non existant.")
  ta = taa.content
  import json
  my_streee = ta.decode()
  my_lffst = json.loads(my_streee)
  endage = my_lffst['created'][0:10]

  yr = int(endage[0:4])
  mn = int(endage[5:7])
  dy = int(endage [8:10])
    
  from datetime import datetime, timedelta
  particular_date = datetime(yr, mn, dy)
  new_date = datetime.today() - particular_date
  age = str(new_date.days)
  print("User Info:")
  print("_________")
  print()
  print("Username: " + theiruser)
  print("ID: " + str(my_list['Id']))
  print("Account Age: " + age)
  print("Online?: [ONLINE IS TEMP DISABLED]")

  t = Groups.groupList(my_list['Id'])

  import json
  my_string = t.decode()
  my_list = json.loads(my_string)
  print("Searching...")
  import time
  time.sleep(1)
  print("Groups:")
  print("_________")
  print()
  def hell(no):
    try:
      print(my_list[no]['Name'])
    except:
      pass
  num = 0
  for c in range(230):
    hell(num)
    num = num + 1
  print("___________________")
  print("___________________")
  print()
