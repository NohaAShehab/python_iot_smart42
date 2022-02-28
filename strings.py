
# name = "Ahmed"
# print(name[2])
#
# # ######## get length of the name
# print(len(name))


# work = "information Technology Institute"
# # print(work[2:8]) # from index 2 to 8-1
# # print(work[100])  # runtime error --> stop execution
# # print("python")
# # print("Hello Islam")
# print(work.count("i"))

# fname = "Noha "
# mid = "Abd El-Hady "
# lastname = "Shehab"
# # ### plus with string means concatination
# # fullname = fname + mid + mid + lastname
# # print(fullname)
# fullname = fname + mid*2 + lastname
# print(fullname)
# ############################
# greet = "Welcome to your first python course provided by @, Hi @   @   @"
# print(greet.replace("@", "iti", 2))
# # print(greet.replace("#", "Khloud"))

# ############################### strip
# greet = "                   Good morning                 "
# print(len(greet))
# print("---------------------------------------")
# # newstr= greet.strip()  # remove space from the string
# # print(newstr)
# # print(len(newstr))
#
# newstr= greet.strip("g ")  # remove space from the string
# print(newstr)
# print(len(newstr))

# greet = "                   Good morning                 "
# # lgreet =greet.lstrip(" G") ## remove
# lgreet =greet.rstrip(" G") ## remove
# print(lgreet)
# print(len(lgreet))
# ########################## formating
name = "Islam"
course = "Python"
# format the string template, contain places need to be replaced with the desired
# t = "Good morning {0} , Nice to meet you in {1} course  {2}"
# # print(t.format(name, course, "."))
# # print(t.format("Ali", course, "."))
# print(t.format(course, name, "."))
###########################################
# t = "Good morning {std_name} , Nice to meet you in {std_course} course {end}"
# print(t.format(end='$',std_name="noha",std_course="python"))
########################## f-format, string
# name = "noha"
# company = "iti"
# year = 2019  # int
# msg = f"Good morning, I am {name}, I works at {company} since {year}"
# print(msg)
# t = True
# # ############ concatination
# # msg = "Good morning I am "+name + "  , I works at "+company + " since "+year + t
# # print(msg)
############################ Numbers
x = 4 + 5j
print(type(x))
y= complex(6,7)
print(y)
print(type(y))



