import os
import json

#Server Configuration
with open ("config.json") as json_file:
  json_date = json.load(json_file)
  server = json_data["server"]["host"]
  
  def magiclogout():
    while True:
      username=(input("username:>")
      print("")
      os.system("C:\\Windows\System32\\  "+username+" /server:"+server)
                print("")
      session = (input("session name or id to logoff:>"))
      os.system("C:\\Windows\\System32\\logoff.exe "+ session+ " /server:"+server)
      os.system("cls")
      print(username+ "logoff")
print(""" 
	        Qrdp disconnect session by:xLeg4cy and Bursoft
			                                        """ )
                
magiclogout()
