#libraries
#json to read the json file, getopt to read the command line arguments, sys to read the system inputs
import getopt, sys
import json
 
#what is argv[1:]
argumentList = sys.argv[1:]

#why json_file, country code is none
json_file = None
country_code = None
try:
    #what are arguments,values
    arguments, values = getopt.getopt(argumentList, "c:f:",["countryCode=","json_file="])

    #why did we write currentArg,Values
    for currentArgument, currentValue in arguments:
        if currentArgument in ['-c','--countryCode']:
            country_code=currentValue
        elif currentArgument in ['-f', '--json_file']:
            json_file=currentValue
     
     #what is expect
except getopt.error as err:
    print (str(err))
    sys.exit()

    #this is for if we didn't find any json file
if json_file is None:
    print("No json file provided")
    sys.exit()

    #why is it open?
with open(json_file) as file_path:
  json_data = json.load(file_path)
#did we have to define the data somewhere to say data in here?
country_code_data = json_data['data']

if country_code is None:
    print("No country codes provided")
    sys.exit()

country_code_list = country_code.split(",")
#country code list for multiple inputs
for cc in country_code_list:
  try:
      print("Country name for country code "+ cc+ " is " +country_code_data[cc]['name'])

  except:
      print("No country name found for country code ", cc)



