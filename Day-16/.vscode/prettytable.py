from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon", ["Chespin", "Fennekin",
                             "Froakie", "Talonflame", "Pikachu", "Swalot"])
table.add_column("Type", ["Grass", "Fire", "Water",
                          "Fire/Flying", "Electric", "Poison"])
print(table)
