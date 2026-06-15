** start of main.py **

def add_setting(setting_dict, setting_pairs):
    #unpack tuple and convert it into lowercase
    key = str(setting_pairs[0]).lower()
    value = str(setting_pairs[1]).lower()

    #check if the key exsists
    if key in setting_dict:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        #add the key-value pairs

        setting_dict[key] = value

        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(setting_dict, setting_pair):
    #convert tuple to lowercase
    key = str(setting_pair[0]).lower()
    value = str(setting_pair[1]).lower()

    #check if it exsists in the dictionary
    if key in setting_dict:
        #update the value in dict
        setting_dict[key] = value

        return f"Setting '{key.lower()}' updated to '{value.lower()}' successfully!"
    else:
        return f"Setting '{key.lower()}' does not exist! Cannot update a non-existing setting."
    
def delete_setting(setting_dict, setting_key):
    #convert key to lower
    key = setting_key.lower()

     #check if key exsists and delete key-value pair
    if key in setting_dict:
        setting_dict.pop(key)
        return f"Setting '{key.lower()}' deleted successfully!"
    else:
        return f"Setting not found!"

def view_settings(setting_dict):
    if not setting_dict:
        return f"No settings available."
    else:
        output = ""
        for key, value in setting_dict.items():
            output += f"\n{key.capitalize()}: {value}"
        return f"Current User Settings:{output}\n"

test_settings = {
    "Theme": "dark"
    }
test_pairs = ("birl", "ball")

print(delete_setting(test_settings, "Theme"))

    




** end of main.py **

