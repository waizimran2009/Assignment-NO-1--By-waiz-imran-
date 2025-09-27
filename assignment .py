# --------------------------------------
# 📘 PYTHON ASSIGNMENT NO 1 (By Waiz Imran)
# --------------------------------------

# ===============================
# QUESTION NO 1
# Print Your Name with Father name and Date of Birth
# ===============================

print( "="*50)
print("📌 QUESTION 1: PERSONAL INFO")
print("="*50)

print("My name is:\nWaiz Imran \nMy Father's name is:\nImran Quresh \nMy Date of Birth is:\n6 Aug 2009")


print("="*50)


# ===============================
# QUESTION NO 2
# Write small bio using variables and print it
# ===============================

print("="*50)
print("📌 QUESTION 2: BIO DATA")
print("="*50)

# Variables for bio
name, age, hobby, goal = "Waiz", 18, "Coding", "To become a successful Python Developer and Cloud Data Engineer"
# Printing using formatted string

print(f"My name is {name}.\nI am {age} years old.\nMy hobby is {hobby}.\nMy biggest goal is {goal}.")
print("="*50)


# ===============================
# QUESTION NO 3
# Demonstrating all Python Operators
# ===============================

print("="*50)
print("📌 QUESTION 3: OPERATORS IN PYTHON")
print("="*50)

# ---------- Arithmetic Operators ----------
print("🔹 1) Arithmetic Operators")
a, b = 10, 2
print(f"a = {a}, b = {b}")
print(f"a + b = {a+b}")
print(f"a - b = {a-b}")
print(f"a * b = {a*b}")
print(f"a / b = {a/b}")
print(f"a // b = {a//b}")
print(f"a % b = {a%b}")
print(f"a ** b = {a**b}")

# ---------- Relational Operators ----------
print("🔹 2) Relational Operators")
a, b = 6, 9
print(f"a = {a}, b = {b}")
print(f"a == b → {a==b}")
print(f"a != b → {a!=b}")
print(f"a > b → {a>b}")
print(f"a < b → {a<b}")
print(f"a >= b → {a>=b}")
print(f"a <= b → {a<=b}")

# ---------- Assignment Operators ----------
print("🔹 3) Assignment Operators")
num = 10
print(f"Initial num = {num}")
num += 5; print(f"After += 5 → {num}")
num -= 3; print(f"After -= 3 → {num}")
num *= 2; print(f"After *= 2 → {num}")
num /= 4; print(f"After /= 4 → {num}")
num //= 2; print(f"After //= 2 → {num}")
num %= 3; print(f"After %= 3 → {num}")
num **= 3; print(f"After **= 3 → {num}")

# ---------- Logical Operators ----------
print("🔹 4) Logical Operators")
p, q = True, False
print(f"p = {p}, q = {q}")
print(f"p and q → {p and q}")
print(f"p or q  → {p or q}")
print(f"not p   → {not p}")
print(f"not q   → {not q}")


# ===============================
# QUESTION NO 4
# Student Marks, Total, Percentage
# ===============================

print( "="*50)
print("📌 QUESTION 4: STUDENTS MARKS CALCULATION")
print("="*50)

# Variables for marks
English, Islamiat, Maths = 78, 91, 68
total_marks = 300
obtained_marks = English + Islamiat + Maths
percentage = (obtained_marks / total_marks) * 100

# Display Results neatly aligned
print(f"{'English:'} {English}/100")
print(f"{'Islamiat:'} {Islamiat}/100")
print(f"{'Maths:'} {Maths}/100")
print("-"*50)
print(f"{'Total Marks:'} {obtained_marks}/{total_marks}")
print(f"{'Percentage:'} {percentage}%")

print("="*50)


