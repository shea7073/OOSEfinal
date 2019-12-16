class Plate:
    def __init__(self, color: str, value: float):
        self.color = color
        self.value = value

    def getColor(self) -> str:
        return self.color

    def getValue(self) -> float:
        return self.value
