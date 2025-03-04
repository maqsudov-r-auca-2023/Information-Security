name = "john"
surname = "doe"
birth_year = "1990"

variations = [
    name, surname, birth_year,
    name + birth_year, surname + birth_year,
    name + "123", surname + "123",
    name.capitalize(), surname.capitalize(),
    name + "!" + birth_year
]

with open("custom_passwords.txt", "w") as f:
    for password in variations:
        f.write(password + "\n")
