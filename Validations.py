import datetime
#Aquí se harán las validaciones

#1. Validar string.

def validate_string(message):
    text = input(message).strip().title()
    while not text:
        print("\n🔴 Error, this field is required. Try again.")
        text = input(message).strip().title()
    return text

#2. validar números.
def validate_number(message):
    number = input(message).strip()
    while not number or not number.isnumeric():
        if not number:
            print("🔴 Error, this field is required. Try again.")
        else:
            print('🔴 Error, you can only enter numbers.')
            
        number = input(message).strip()
    
    return str(number)

#3. Validar nombre del usuario
def validate_name(message):
    name = input(message).strip()
    while not name or not all(na.isalpha() or na.isspace() for na in name):
        if not name:
            print("🔴 Error, this field is required. Try again.")   
        else:
            print('🔴 Error, you must enter a valid data. Try again.') 
        
        name = input(message).strip()
                               
    return name.title()

def validate_year(message):
    while True:
        year = int(validate_number(message))
        yearAct = datetime.date.today().year
        
        if 1500 <= year <= yearAct:
            return str(year)
        else:
            print(f"🔴 Error, the year must be between 1500 and {yearAct}. Try again")
   
