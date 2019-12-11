import Lifter.py
import Attempt.py

class Judge:

    def __init__(self, lifter: Lifter, attempt: Attempt):
        self.lifter = lifter
        self.attempt = attempt

    def getLifterBeingJudged(self) -> Lifter:
        return self.lifter

    def getAttemptBeingJudged(self) -> Attempt:
        return self.attempt

    def markAttemptRed(self, attempt: Attempt):
        attempt.isAttemptSuccessful = False
        print("The attempt has been redlighted!")

