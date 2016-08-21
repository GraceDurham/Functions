master_list = {"Safeway" : ["garlic", "champagne", "butter"], 
               "Whole Foods": ["cherries"]}

# wine = {"Rodney Strong": "Cabernet", "Alexander Valley" : "Merlot"}
# beer = {"Lagunitas":"Sour", "Trummer":"Pilsner"}

# def main():
  #While True: 
 	

def show_all_list():
 	#to do 
  for store_list in master_list.values():
      store_list.sort()
      print store_list



def show_a_specific_list():
 	#to do 
  return master_list ["whole foods"]
  

def add_new_list(key): 
  key=key.lower()
  master_list["Trader Joes"] =[]
  if key not in master_list:
    master_list[key]=shopping_list 
  else: 
    print "A list with that name already exists!"
  return master_list

def add_item(key, item):
  item=item.lower()
  key=key.lower()

  if key in master_list:
   	 shopping_list=master_list[key]

  if item not in master_list:
    	shopping_list.append(item)
    	print "Here's your updated list," 
  else:
    	print "This item %s already exists!" % (item)

 	else:
   		 print "There is no list with that name." 



def remove_item(key, item):
  item =item.lower()
  key=key.lower()

    if key in master_list:
    shopping_list=master_list[key]
    if item in shopping_list: 
      shopping_list.remove(item)
      print "%s has been removed. Here's your updated list" % (item)
    else:
     	print "There is no list with that name."

def remove_list_nickname():
	key=key.lower()

	if key in master_list:
  		del master_list["Whole Foods"]
  	return master_list


  def menu_choice():
    print "0 - Main Menu."
    print "1 - Show all lists"
    print "2 - Show a specific lists"
    print "3 - Add a new shopping lists"
    print "4-  Add an item to a shopping list"
    print "5-  remove an item to a shopping list"
    print "6-  remove an item by nickname"
    print "7-  exit when you are done"

    choice=int(raw_input("Please choose from the menu list."))
   	return choice 
	
def main():
  
  choice= menu_choice()

  while True: 
  	if choice==0: 
  		choice=menu_choice()
  	elif choice==1:
  		show_all_list()
  		choice=0 
  	elif choice==2:
  		list_name=raw_input("Which list would you like to see.")
  		print sorted_shopping_list(list_name)
  		choice=0
  	elif choice==3 
  		list_name=raw_input("Enter the name for your list.")
  		add_new_list(list_name)
  		item=raw_input("Please enter an item.")
  		while item.upper() != "x":
  			add_item(list_name,item)
  			item=raw_input("Enter another item or press "x" when done.")
  		choice=0
  	elif choice==4	
  		list_name=raw_input("What's the name of the list?")
  		item=raw_input("Please enter an item.")
  		while item.upper() !="X":
  			add_item(list_name,item)
  			item=raw_input("Enter another item or press "x" when done.")
  		choice=0
  		
  	elif choice==5:
  		list_name=raw_input("What's the name of the list?")
  		item=raw_input("Please enter an item to remove.")
  		while item.upper() !="X":
  			remove_item(list_name, item)
  			item=raw_input("Enter another item or press "x" when done.")
  		choice=0
  	elif choice==6:
  		list_name=raw_input("What's the name of the list?")
  		remove_a_list(list_name)
  		choice=0
  	elif choice==7:
  		break 			


	

if __name__ == '__main__':
		main ()	