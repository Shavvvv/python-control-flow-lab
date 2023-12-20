#python3 functions.py

def say_hello():
    return "Kate"

print(say_hello())


def dev_skills(dev_name,*args) :
    dev= { 'name' : dev_name,  'skills' : list(args)}

    for skill in args:
        dev['skills'].append(skill)

    return dev

print(dev_skills("alex", 'Html', 'css','js'))