import numpy as np

class Modelo:
    def __init__(self, A: np.array, b: np.array, c: np.array) -> None:
        self.A = A
        self.b = b
        self.c = c

    def get_data(self) -> tuple[np.array, np.array, np.array]:
        return self.A, self.b, self.c
    
    def get_coeficiente(self) -> tuple[np.array]:
        return self.c