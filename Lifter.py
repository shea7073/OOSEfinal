
class Lifter:
    wilks : int = 0.0
    def __init__(self, gender: str, bodyWeight: float, age: int, weightClass: int, orm: int):
        self.bodyWeight = bodyWeight
        self.age = age
        self.weightClass = weightClass
        self.orm = orm

    def calculateWilks(self):
        a, b, c, d, e, f = 0.0
        if self.gender == "Male":
            a = -216.0475144
            b = 16.2606339
            c = -0.002388645
            d = -0.00113732
            e = 7.01863E-06
            f = -1.291E-08
        elif self.gender == "Female":
            a = 594.31747775582
            b = -27.23842536447
            c = 0.82112226871
            d = -0.00930733913
            e = 4.731582E-05
            f = -9.054E-08
        else:
            print("ONLY TWO GENDERS EXIST!")

        x = self.bodyWeight

        Lifter.wilks = self.orm * 500 / (a + b * x + c * x**2 + d * x**3 + e * x**4 + f * x**5)



    def getBodyWeight(self) -> float:
        return self.bodyWeight

    def getAge(self) -> int:
        return self.age
