master_list = {"Safeway" : ["garlic", "champagne", "butter"], 
               "Whole Foods": ["cherries"]}

# wine = {"Rodney Strong": "Cabernet", "Alexander Valley" : "Merlot"}
# beer = {"Lagunitas":"Sour", "Trummer":"Pilsner"}

# def main():
  #While True: 
def main_prompt():
    print "0 - Main Menu."
    print "1 - Show all lists"
    print "2 - Show a specific lists"
    print "3 - Add a new shopping lists"
    print "4-  Add an item to a shopping list"
    print "5-  remove an item to a shopping list"
    print "6-  remove an item by nickname"
    print "7-  exit when you are done"


    choice= "0" #raw_input=("Please choose 0,1,2,3,4,5,6,7")
 	

def show_all_list():
 	#to do 
  for store_list in master_list.values():
      store_list.sort()
      print store_list





def show_a_specific_list():
 	#to do 
 	return master_list["Whole Foods"]

def add_new_list(): 
  master_list["Trader Joes"] =[]
  return master_list

def add_item():
  master_list["Safeway"].append("cookie")
  return master_list

def remove_item():
  master_list["Safeway"].remove("cookie")
  return master_list
  	

def remove_list_nickname():
  del master_list["Whole Foods"]
  return master_list
	


def main():
  main_prompt()
  print show_all_list()
  print show_a_specific_list() 
  print add_new_list()
  print add_item()
  print remove_item()
  print remove_list_nickname()

	

if __name__ == '__main__':
		main()	