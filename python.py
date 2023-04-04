# bill = 1000

# discount1 = 100 #Only if the bill is < 1500

# discount2 = 200 #Only if the bill is > 4000

# if bill > 2000 and bill > 4000:
#   print('Bill is greater than 2000')
#   bill = bill - discount1
# elif bill > 2000:
#   print("Bill is greater than 500")
#   bill = bill - discount2

# elif bill < 1500:
#   print("Bill is less than 1500")
#   bill = bill - discount1
# else:
#   print('Bill is less than 2000!')


# print("Net Bill: ", str(bill))


# We are writing an if/elif and else statements for a college grading system.

# grade = 50

# if grade >= 90:
#     print("A")
# elif grade >= 80:
#     print("B")
# elif grade >= 70:
#     print("C")
# elif grade >= 60:
#     print("D")
# else:
#     print("F")

#     MATCH CASE
# A basic implemntation of match case statements looks a lot like if statements in python.
#   Basic Syntax:
# match subject:
#     case <pattern_1>:
#         <action_1>
#     case  <pattern_2>:
#         <action_2>
#     case <pattern_3>:
#         <action_3>
#     case _: #default
#         <action_wildcard>

# Example;

# number = "5"

# match number:
#     case "1":
#         print('one')
#     case "3":
#         print('three')
#     case _:
#         print("invalid")

# Example2;
 
# http_status = 200
# match http_status:
#     case 200:
#         print("Success")