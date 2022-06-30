import json



#fb = open("example_2.txt")

def read_dict(d, name):
    fb = open(name[:-4]+".txt", "w")
    for k, v in d.items():
        if type(v) is dict:
            read_dict(v)
        else:
            fb.write(k+"\n")
            fb.write(v+"\n")
            

def json_to_text(name):
    with open(name, "r") as fa:
        data = json.load(fa)

        

    
    
