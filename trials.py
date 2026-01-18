

attendes = []
def registration_data():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    ticket_type = input("Enter ticket type (Regular/VIP): ")


    def get_attendee_data():
        return {'name':name ,'age':age, 'ticket type':ticket_type}


    def assigning_zone():
        if ticket_type == "VIP":
            return "VIP Zone"
        elif age < 18 and ticket_type == "Regular":
            return "Youth Zone"
        elif age >= 18 and ticket_type == "Regular":
            return "Standard"
        else:
            return "Please try again"

                
    def validation():

        attendee = {
            "name": name,
            "age": age,
            "zone": assigning_zone()
        }
        attendes.append(attendee)
        return "Registration Successful"
    print(validation())
def total():
    vip_count = 0
    regular_count = 0 
    youth_count = 0 
    total_age = 0

    for attendee in attendes:
        total_age += attendee['age']

        if attendee ["zone"] == "VIP Zone":
            vip_count +=1
        elif attendee ['zone'] == "Youth Zone":
            youth_count += 1
        elif attendee ['zone'] == "Standard":
            regular_count += 1

    average_age = total_age / len(attendes)

    return {f"Total VIP attendance : {vip_count} , Youth : {youth_count} , Regular : {regular_count}, Average age : {average_age : 1f}"}
                        



registration_data()
registration_data()
registration_data()

print(total())





