student={
"ayush":{"roll":157, "marks":500, "collage-name":"iibm"},
"karan":{"roll":158, "marks":500,"collage-name":"iibm"},
"bobby":{"roll":158, "marks":500, "collage-name":"iibm"},

}

name=input('enter your name to get marks:')

if name in student:
    print("roll" ,student[name]["roll"])
    print("marks",student[name]["marks"])
    print("collage-name",student[name]["collage-name"])
else:
    print("not found your result...")
