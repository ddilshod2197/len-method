class Masala:
    def __init__(self, nom, qiymat):
        self.nom = nom
        self.qiymat = qiymat

    def __len__(self):
        return len(self.qiymat)

masala = Masala("Masala", "12345")
print(len(masala))  # Chiqaradi: 5
