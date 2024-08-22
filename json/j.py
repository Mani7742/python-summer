# JSON data types are similar to Python data types
# JSON data types are:
# 1. string
# 2. number
# 3. boolean
# 4. array
# 5. object
# 6. null
#------------------------------------------------------------------------------------------------------------------

# Creating JSON
import json
dic = {
    'course_name':"Python",
    'fees':15000
}
# Convert the dictionary into JSON data type
json_data = json.dumps(dic)
print(json_data)  # Output: {"course_name": "Python", "fees":
print(type(json_data))
# The json.dumps() function converts a dictionary into a JSON string.

# Both dictionary and json works on key and value pairs
#--------------------------------------------------------------------------------------------------------------

#Converting JSON into python Objects

j = '{"cname":"Python","Duration":"2 months"}'
json_convert = json.loads(j)
print(json_convert)  # Output: {'cname': 'Python', 'Duration': '2 months
print(type(json_convert))