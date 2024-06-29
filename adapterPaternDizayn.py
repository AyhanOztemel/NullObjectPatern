from abc import ABC,abstractmethod

class IElectricalAppliances(ABC):
    @abstractmethod
    def plugAndRun(self):
        pass

class Refrigerator(IElectricalAppliances):   
    def __init__(self):
        self.volt=220
    
    def plugAndRun(self):
        print("refrigerator started....")
        print("self.volt----->",self.volt)
        return self.volt
    
#We have electrical outlets that provide 220 volt output.
class PowerPoint():
    def __init__(self,electricalAppliances:IElectricalAppliances):
        print("id--->",electricalAppliances)
        self.volt=electricalAppliances.plugAndRun()
#---------------------------------------------------    
class IMobilePhone(ABC):
    @abstractmethod
    def mobilCharge(self):
        pass
  
class MobilePhone(IMobilePhone):   
    def __init__(self):
        self.volt=5
    
    def mobilCharge(self):
        print("mobile phone is charging....")
        print("self.volt----->",self.volt)
        return self.volt
    
#We adapt our electrical devices operating at different voltages to the existing socket    
class Adapter(IElectricalAppliances):
    def __init__(self,mobilePhone:IMobilePhone):
        self.mobilePhone=mobilePhone
    
    def plugAndRun(self):
       return self.mobilePhone.mobilCharge()      
#---------------------------------------------------        
class IComputer(ABC):
    @abstractmethod
    def computerCharge(self):
        pass       
class Computer(IComputer):   
    def __init__(self):
        self.volt=19
    
    def computerCharge(self):
        print("computer started....")
        print("self.volt----->",self.volt)
        return self.volt
# We adapt our electrical devices operating at different voltages to the existing socket   
class Adapter2(IElectricalAppliances):
    def __init__(self,computer:IComputer):
        self.computer=computer
    
    def plugAndRun(self):
       return self.computer.computerCharge()       

#---------------------------------------------------        
refrigerator=Refrigerator()
powerPoint= PowerPoint(refrigerator)

samsung=MobilePhone()
adapter=Adapter(samsung)
powerPoint=PowerPoint(adapter)

computer= Computer()
adapter2=Adapter2(computer)
powerPoint= PowerPoint(adapter2)
