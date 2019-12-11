
class Attempt:
    isAttemptSuccessful : bool = True
    def __init__(self, weightLifted: float, attemptNumber: int):
        self.weightLifted = weightLifted
        self.attemptNumber = attemptNumber


    def isAttemptRed(self) -> bool:
        if Attempt.isAttemptSuccessful:
            return True
        else:
            return False

    def getWeightLifter(self) -> float:
        return self.weightLifted

    def attemptNumber(self) -> int:
        return self.attemptNumber

