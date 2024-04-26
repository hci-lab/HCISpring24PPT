from dollarpy import Recognizer, Template, Point

# Define 'Template' gestures, each consisting of a name and a list of 'Point' elements.
# These 'Point' elements have 'x' and 'y' coordinates and optionally the stroke index a point belongs to.
tmpl_1 = Template('X', [
    Point(0, 0, 1),
    Point(1, 1, 1),
    Point(0, 1, 2),
    Point(1, 0, 2)])
tmpl_2 = Template('line', [
    Point(0, 0),
    Point(1, 0)])

HCILec=Template('HCI',[
    Point (100,450,1),
    Point (102,460,1),
    Point (103,470,1)
])

HCILec1=Template('HCI1',[
    Point (100,450,1),
    Point (102,470,1),
    Point (103,480,1)
])

# Create a 'Recognizer' object and pass the created 'Template' objects as a list.
recognizer = Recognizer([tmpl_1, tmpl_2,HCILec,HCILec1])

# Call 'recognize(...)' to match a list of 'Point' elements to the previously defined templates.
result = recognizer.recognize([
    Point( 100, 450, 1),
    Point(102, 460, 1),
     Point (103,480,1)
    ])
print(result)  # Output: ('X', 0.733770116545184)