# 2. What is the output of this -


class Mother:
    def cook(self):
        print('Can cook pasta')


class Father:
    def cook(self):
        print('Can cook noodles')


class Daughter(Father, Mother):
    pass


class Son(Mother, Father):
    def cook(self):
        super().cook()
        print('Can cook butter chicken')


d = Daughter()
s = Son()

d.cook()
print()
s.cook()

# This will be the output- Super method follows the MRO- Method Resolution Order where they are checked from left to
# to right- For daughter the first checking point would be Father Class- So if Father class has the cook method then
# it display it, if it's not present goes to the Mother Class. Same for son, as the left checking point would be mother
# it executed the cook() method from Mother.


# can cook noodles

# can cook pasta
# can cook butter chicken