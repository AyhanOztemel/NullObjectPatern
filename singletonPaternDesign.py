class Singleton:
    instance = None

    def __new__(cls):
        if not cls.instance:
            cls.instance = super().__new__(cls)
        return cls.instance
    
class NotSingleton():
    pass

#Example

#When using NotSingleton Class the output of the id instance id is the defferent

notSingleton1=NotSingleton()
print("notSingleton1 ----->"+str(id(notSingleton1)))

notSingleton2=NotSingleton()
print("notSingleton2 ----->"+str(id(notSingleton2)))

notSingleton3=NotSingleton()
print("notSingleton3 ----->"+str(id(notSingleton3)))

print("*************************************")

#When using Singleton Class the output of the instance id is the same

singleton1=Singleton()
print("singleton1 ----->"+str(id(singleton1)))

singleton2=Singleton()
print("singleton2 ----->"+str(id(singleton2)))

singleton3=Singleton()
print("singleton3 ----->"+str(id(singleton3)))

