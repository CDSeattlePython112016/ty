students = [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


# def get_names(d):
#     for item in d:
#         print item["first_name"], item["last_name"]

for item in students:
    print item["first_name"], item["last_name"]




users = {
 'Students': [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def get_user_len(context):
    for key, data in context.items():
            print key
            count = 0
            for value in data:
                count += 1
                charNum =  len(value["first_name"]) + len(value["last_name"])
                print count, "-", value["first_name"], value["last_name"],"-",charNum  
get_user_len(users)