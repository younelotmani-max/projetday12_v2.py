admins = ["Younes", "Rayane", "Ahlam"]
company_hq = ("Zurich", "Google", 15000)
city, company, base_salary = company_hq
required_skills = {"python", "sql", "ai"}
user_profile = {}


admin_pass = "zurich2026"
tries = 3

print("=" * 60)
print(" Security Core Google Zurich AI SYSTEME ")
print("=" * 60)

name = input(" Please enter your name: ").strip().capitalize()
email = input(" And your Gmail: ").strip()
username = email[:email.index("@")]
domain_name = email[email.index("@") + 1:]
age = int(input(" Your Age: ").strip())

print(f"Your name is {name} \nYour gmail {email} \nYour username {username} \nYour age {age} \nYour domain {domain_name}")
print("=" * 80)

skills = input(" What is your skill in coding: ").strip().lower()

if age >= 18:
    print(" Eligible")
else:
    print(" Underage")


if name in admins:
    print(f" Admin {name} detected! Security verification required.")
    the_pass = input(" Enter Admin Password: ").strip()

    while the_pass != admin_pass:
        tries -= 1
        if tries == 0:
            print(" SYSTEM LOCKED! Too many failed attempts. Shutting down...")
            exit()  
        print(f" Wrong password! You have {tries} tries left.")
        the_pass = input("🔑 Try again: ").strip()

    print(f" Welcome Admin {name}! Full System Access Granted.")

    option = input(" Delete or update or add: ").strip().lower()

    if option == "update":
        thenewname = input("Your new name please: ").strip().capitalize()
        admins[admins.index(name)] = thenewname
        print(f" Name updated. Admins list: {admins}")

    elif option == "delete":
        admins.remove(name)
        print(f" Name deleted. Admins list: {admins}")

    elif option == "add":
        newname = input("New admin name: ").strip().capitalize()
        admins.append(newname)
        print(f" Admin added. Admins list: {admins}")

else:
    print(f" Welcome Candidate {name}!")

final_salary = base_salary

if skills in required_skills and age >= 18:
    final_salary += 5000
    print(f" Accepted as Senior! Your salary with bonus is: ${final_salary}")
    print(f" Remaining skills to learn: {required_skills - {skills}}")

elif skills in required_skills or age >= 18:
    print(f" Accepted as Junior Trainee! Your salary is: ${final_salary}")

else:
    print(" Application Pending: You need to upgrade your skills.")

unit = input(" Please choose: Months, Weeks, Days, Hours: ").strip().lower()

months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24

if unit == "months" or unit == "m":
    print(f"Your age is {months} months.")
elif unit == "weeks" or unit == "w":
    print(f"Your age is {weeks} weeks.")
elif unit == "days" or unit == "d":
    print(f"Your age is {days} days.")
elif unit == "hours" or unit == "h":
    print(f"Your age is {hours} hours.")

user_profile = {
    "Name": name,
    "Username": username,
    "Domain": domain_name,
    "Age": age,
    "Final_Salary": final_salary
}

print("=" * 60)
print(" FINAL AI DOSSIER:")

for key in user_profile:
    print(f"🔹 {key} : {user_profile[key]}")
print("=" * 60)



