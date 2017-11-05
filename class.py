#!/usr/bin/python3

#Filename : class.py

class Robot:
    population = 0

    def __init__(self, name):
        self.name = name

        print('Initialization of {0}'.format(self.name))
        Robot.population += 1

    def __del__(self):
        '''The dying robot'''

        print('{0} is being destroyed'.format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print ('{0} was the last one'.format(self.name))

        else :
            print('There are still {0:d} robots working'.format(Robot.population))

    def sayHi(self):
       '''Greetings by my Robot'''

       print('Hi!, My master calling me {0}'.format(self.name))

    def howMany():
        print('We have {0:d} robots.'.format(Robot.population))
    howMany = staticmethod(howMany)



droid1 = Robot('R2-D2')
droid1.sayHi()
Robot.howMany()

droid2 = Robot('CP9')
droid2.sayHi()
Robot.howMany()

print('Goodbye Robots!')

del droid1
del droid2

Robot.howMany()


