# Week 1.2, Session 2: Task 6
################FUNCTIONS####################

def Output(temp_status, pressure_status):
    output = ""

    if (status == 1): #machine operating
        match temp_status:
            case 3:
                output = "too high. Shutting down the system is recommended."
                if (pressure_status == 3):
                    output = "Both pressure and temperature are " + output
                elif (pressure_status == 2):
                    output = "Pressure is fine but temperature is " + output
                else:
                    output = "Pressure is low but but temperature is " + output
            case 2:
                if (pressure_status == 3):
                    output = "Temperature is fine but pressure is high. Maintenence is recommended."
                elif (pressure_status == 2):
                    print("Machine is operating normally. No action needed.")
                else:
                    output = "Pressure is low but but temperature is fine. No action needed."
            case 1:
                if (pressure_status == 3):
                    output = "Temperature is low but pressure is high. Maintenence is recommended."
                elif 



print("Pressure is high. Maintenence is recommended.")
print("Temperature is low. No action needed")
print("Pressure is low. Machine is operating normally.")

print("Machine is not operating. No action needed. ")




def Get_Temp_Status():
    if (temp < 50): #low
        temp_status = 1
    elif (temp < 80): #mid
        temp_status = 2
    else: #high
        temp_status = 3

    return temp_status

def Get_Pressure_Status():
    if (pressure < 70): #low
        pressure_status = 1
    elif (pressure < 100): #mid
        pressure_status = 2
    else: #high
        pressure_status = 3

    return pressure_status


#################PROGRAM###################
temp = int(input("Enter an integer value for the system temperature in celcius: "))
pressure = int(input("Enter an integer value for the system pressure in PSI: "))
status = int(input("Enter the operational status of the system(1 = On, 0 = Off): "))

valid = False

#input validation
while (not valid):
    if (temp.is_integer):
        valid = True
    else:
        valid = False
        temp = int(input("Invalid temperature value. Please enter an integer: "))

    if (pressure.is_integer):
        valid = True
    else:
        valid = False
        pressure = int(input("Invalid pressure value. Please enter an integer: "))

    if (status.is_integer):
        valid = True
        if (status != 0 or status != 1):
            status = int(input("Invalid status value entered: Please enter either 0 or 1: "))
    else:
        status = int(input("Invalid status value entered. Please enter an integer: "))


# pressure and temperature statuses
# low = 1
# mid = 2
# high = 3

Output(Get_Temp_Status(), Get_Pressure_Status())






















