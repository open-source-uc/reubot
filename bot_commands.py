import json

def get_current_list():
    selected = open('current_list.json', 'r+')
    current_list = json.load(selected)
    selected.close()
    
    if current_list["current_list"] != "":
        data = current_list["current_list"]
        return(f"{data}")
    else:
        return(None)


def set_current_list(list_name:str):
    lists = open('lists.json', 'r+')
    list_object = json.load(lists)
    lists.close()

    if list_name in list_object.keys() or list_name == "":
        list_object[list_name] = []

        selected_list = open('current_list.json', 'r+')
        current_list = json.load(selected_list)
        selected_list.close()

        current_list["current_list"] = list_name

        #Rewrite values without deleted list
        json_file = open('current_list.json', 'w+')
        json_file.write(json.dumps(current_list, indent=4))
        json_file.close()

        return(f"{list_name} has been set as the current list")
    else:
        return (f"List {list_name} does not exist")

def create_list(list_name:str):
    lists = open('lists.json', 'r+')
    list_object = json.load(lists)
    lists.close()

    #Create list by name
    if list_name in list_object.keys():
        return(f"List {list_name} already exists")
    else:
        list_object[list_name] = []

        #Rewrite values without deleted list
        json_file = open('lists.json', 'w+')
        json_file.write(json.dumps(list_object, indent=4))
        json_file.close()
        set_current_list(list_name)
        return (f"List {list_name} has been created successfully and is now the currently selected list")
    


def delete_list(list_name:str):
    lists = open('lists.json', 'r+')
    list_object = json.load(lists)
    lists.close()
    if list_name in list_object.keys():

        #Delete list by name
        del list_object[list_name]

        #Rewrite values without deleted list
        json_file = open('lists.json', 'w+')
        json_file.write(json.dumps(list_object, indent=4))
        json_file.close()
        return(f"List {list_name} has been deleted successfully")
    else:
        return(f"List {list_name} not exist")      


def add_bullet(list_name:str, description:str, checked:str = "unchecked"):
    lists = open('lists.json', 'r+')
    list_object = json.load(lists)
    
    if list_name in list_object.keys():
        bullet_id = len(list_object[list_name])

        if checked == "checked":
            checked = True
        else:
            checked = False

        bulletpoint = {
            "id": bullet_id, 
            "description":  description, 
            "checked": checked
        }

        list_object[list_name].append(bulletpoint) 

        #Rewrite values
        json_file = open('lists.json', 'w+')
        json_file.write(json.dumps(list_object, indent=4))

        lists.close()
        json_file.close()

        return("Bullet added successfully")
    else:
        return(f"List {list_name} does not exist")


def delete_bullet(list_name:str, bullet_id:str):
    lists = open('lists.json', 'r+')
    list_object = json.load(lists)
    lists.close()

    #Delete list by name
    if int(bullet_id) < len(list_object[list_name]):
        del list_object[list_name][int(bullet_id)]

        for i in range(len(list_object[list_name])):
            print(i)
            list_object[list_name][i]["id"] = i

        #Rewrite values without deleted list
        json_file = open('lists.json', 'w+')
        json_file.write(json.dumps(list_object, indent=4))
        json_file.close()
        return(f"Bullet {bullet_id} has been deleted succesfully")
    else:
        return("This bullet does not exist")


def update_bullet(list_name:str, bullet_id:int, description:str):
    lists = open('lists.json', 'r+')
    list_object = json.load(lists)
    lists.close()

    if list_name in list_object.keys():
        if int(bullet_id) < len(list_object[list_name]):
            #Update list by name
            list_object[list_name][int(bullet_id)] = {
                "id": bullet_id, 
                "description":  description, 
                "checked": list_object[list_name][int(bullet_id)]["checked"]
            }
        
            #Rewrite values
            json_file = open('lists.json', 'w+')
            json_file.write(json.dumps(list_object, indent=4))
            json_file.close()
            return(f"Bullet {bullet_id} has been updated")
        else:
            return(f"Bullet {bullet_id} not exist")
    else:
        return(f"Bullet {bullet_id} not exist")


def checked(list_name:str, bullet_id:str, checked:bool):
    lists = open('lists.json', 'r+')
    list_object = json.load(lists)
    lists.close()

    if list_name in list_object.keys():
        if int(bullet_id) < len(list_object[list_name]):
            #Update list by name
            list_object[list_name][int(bullet_id)]["checked"] = checked
        
            #Rewrite values
            json_file = open('lists.json', 'w+')
            json_file.write(json.dumps(list_object, indent=4))
            json_file.close()
            return(f"Bullet {bullet_id} has been updated")
        else:
            return(f"Bullet {bullet_id} not exist")
    else:
        return(f"Bullet {bullet_id} not exist")


def print_list(list_name:str):
    formatted_bullets = ''
    lists = open('lists.json', 'r+')
    list_object = json.load(lists)
    if list_name in list_object.keys():
        formatted_bullets += list_name + ':\n'
        for i in range(len(list_object[list_name])):
            current_object = list_object[list_name][i]
            formatted_bullets += str(current_object["id"]) + "."
            if current_object["checked"]:
                formatted_bullets += " [x] "
            else:
                formatted_bullets += " [  ] "
                
            formatted_bullets += current_object["description"] + " \n"

        lists.close()
        return(formatted_bullets)

        #Rewrite values without deleted list
    else:
        lists.close()  
        return(f"List {list_name} not exist")


def view_all_lists():
    lists = open('lists.json', 'r+')
    list_object = json.load(lists)
    lists.close()
    
    list_data = 'ALL LISTS: \n'

    if len(list(list_object.keys())) > 0:
        for item in list(list_object.keys()):
            list_data += "- " + item + "\n"
        return(list_data)
    return("There are currently 0 lists. Create one by using the '/create [list_name]' command")