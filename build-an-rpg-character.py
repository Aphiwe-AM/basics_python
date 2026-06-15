

full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return "The character name should be a string"
    elif name == "":
        return "The character should have a name"
    elif len(name) > 10:
        return "The character name is too long"
    elif name.find(" ") != -1:
        return "The character name should not contain spaces"
    
    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return "All stats should be integers"
    elif strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"
    elif strength > 4 or intelligence > 4 or charisma > 4:
        return"All stats should be no more than 4"
    elif strength + intelligence + charisma != 7:
        return "The character should start with 7 points"



    str_full_dot = full_dot * strength
    int_full_dot = full_dot * intelligence
    cha_full_dot = full_dot * charisma
    

    def find_empty(stat):
        return 10 - stat

    
    str_empty_dot = empty_dot * find_empty(strength)
    int_empty_dot = empty_dot * find_empty(intelligence)
    cha_empty_dot = empty_dot * find_empty(charisma)
    
    total_str_dots = str_full_dot + str_empty_dot
    total_int_dots = int_full_dot + int_empty_dot
    total_cha_dots = cha_full_dot + cha_empty_dot

    return f"{name}\nSTR {total_str_dots}\nINT {total_int_dots}\nCHA {total_cha_dots}"

    

print(create_character("ren", 4, 4, 4))
