#Task 1

class vehicle:
    def __init__(self, registration_number, vehicle_type, owner):
        self.reg_number = registration_number
        self.vehicle_type = vehicle_type
        self.owner = owner
        
    def updateOwner(self, new_owner):
        self.owner = new_owner
        
    def info(self):
        print(f"This is {self.owner}'s {self.vehicle_type} with registration number {self.reg_number}.")
        
sammy_vehicle = vehicle(111111, "car", "Sam")
jims_vehicle = vehicle(222222, "truck", "Jim")
billys_vehicle = vehicle(333333, "14-wheeler", "Billy")
sammy_vehicle.info()
jims_vehicle.info()
billys_vehicle.info()

#Task 2 
class event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participants = []
        
    def addParticipant(self, participant_name):
        self.participants.append(str(participant_name))
    
    def getParticipantCount(self):
        print(f"{self.name} has {len(self.participants)} participants.")
        participants = [guest for guest in self.participants]
        print("\n".join(participants))
        
party = event("Billy's birthday party", "July 30th")
for name in ["Jim", "Timmy", "Bobby", "Sammy"]:
    party.addParticipant(name)
    
party.getParticipantCount()
        