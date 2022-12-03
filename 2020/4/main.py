with open("input.txt", "r") as f:
    data = [item for item in f]

passport = {}
valid_passports_one_star, valid_passports_two_star = 0, 0
for line in data:
    passport.update(
        {item.split(":")[0]: item.split(":")[1] for item in line.strip().split()}
    )
    if not line.strip() or line == data[-1]:
        if len(passport) == 8 or len(passport) == 7 and "cid" not in passport:
            valid_passports_one_star += 1
            valid_passports_two_star += (
                1920 <= int(passport["byr"]) <= 2002
                and 2010 <= int(passport["iyr"]) <= 2020
                and 2020 <= int(passport["eyr"]) <= 2030
                and passport["hcl"][1:].isalnum()
                and passport["hcl"][0] == "#"
                and passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                and len(passport["pid"]) == 9
                and ("cm" in passport["hgt"] or "in" in passport["hgt"])
                and (
                    (
                        59 <= int(passport["hgt"][:-2]) <= 76
                        and passport["hgt"].endswith("in")
                    )
                    or (
                        150 <= int(passport["hgt"][:-2]) <= 193
                        and passport["hgt"].endswith("cm")
                    )
                )
            )
        passport = {}

print(valid_passports_one_star, valid_passports_two_star)
