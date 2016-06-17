class Fizzbuzz:

    def __init__(self):
        self.mapping = []

    def fizzbuzz(self, number):
        output = ''.join(w for m, w in self.mapping if not number % m)
        return output + '!' if output else str(number)

    def add_rule(self, multiple, output):
        self.mapping.append((multiple, output))
        self.mapping = sorted(self.mapping, key=lambda i: i[0])
