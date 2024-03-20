import queue


class Coda_prioritaria:
    def __init__(self):
        self._lista = []

    def push(self, valore):
        self._lista.append(valore)

    def pop(self):
        """
        Restituisce il valore minimo presente nella lista e lo cancella
        :return:
        """

        "[2, 5, 1, 9]"
        "enumerate restituisce [(0,2), (1,5), (2,1), (3,9)]"
        "[2, 5, 1, 9] è la lista su cui calcolo il minimo"

        pos_min, val_min = min(enumerate(self._lista), key=lambda t: t[1])
        self._lista.pop(pos_min)
        return val_min


c = Coda_prioritaria()
c.push((2, "Paolo"))
c.push((1, "Giulia"))
c.push((2, "Antonio"))
print(c.pop())
c.push((1, "Anna"))
print(c.pop())
print(c.pop())
print(c.pop())

coda = queue.PriorityQueue()

coda.put((2, "Paolo"))
coda.put((1, "Giulia"))
coda.put((2, "Antonio"))
print(coda.get())
coda.put((1, "Anna"))
print(coda.get())
print(coda.get())
print(coda.get())
