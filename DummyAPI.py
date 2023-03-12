from requests import *
from skimage import io
from keyboard import *
from json import *

jsonid= []
reques = None
req = []
url = ["https://hub.dummyapis.com/employee?noofRecords=10&idStarts=1001"]
def main():
    for i in range(len(url)):
        reques = get(url[i]).text
        
        req.append(reques)
        jsonid.append(loads(req[i]))
        everything = ""
        for j in jsonid[i][i].values():
            everything = everything + str(j) + " "
        everything = everything.split(" ")
        for i in everything:
            print(i)
        io.imshow(io.imread(str(everything[1])))
        io.show()
    
if __name__ == "__main__":
    running = True
    main()
    while running:
        if is_pressed("q") or is_pressed("escape"):
            running=False
