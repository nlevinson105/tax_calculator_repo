class Taxpayer:

    def __init__(self, name, age, income):
        self.name = name
        self.age = age
        self.income = income


class Spouse(Taxpayer):

    def __init__(self, name,  age, income, spouse=None):
        super().__init__(name, age, income)

        if spouse is None:
            self.spouse = []
        else:
            self.spouse = spouse

    def add_spouse(self, tp):
        if tp not in self.spouse:
            self.spouse.append(tp)

    def get_spouse(self):
        for tp in self.spouse:
            return tp.name


tp1 = Taxpayer('Nate', 27, 100000)
tp2 = Spouse('Nuria', 27, 50000, None)
print(tp1.name)
print(tp1.income)
print(tp2.name)
print(tp2.income)
tp2.add_spouse(tp1)
print(tp2.get_spouse())

household_inc = tp1.income + tp2.income
print(household_inc)
















