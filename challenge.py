import json

def main():

    with open("challenge.json","r") as vfile:
        datadictionary = vfile.read()
    
    datadecode = json.loads(datadictionary)

    print("name: ", datadecode[3]['name'])
    print("eye color: ", datadecode[3]['eyeColor'])
    print("favorite fruit", datadecode[3]['favoriteFruit'])


for person in range(len(datadecode)):
    print("Name: ",datadecode[person]['name'])
    print("Email: ", datadecode[person]['email'])
    print("Phone: ", datadecode[person]['phone'])
    print("Addresss: ", datadecode[person]['address'])
    for pal in datadecode[person]['friends']:
        print(datadecode[person]['friends']['name'])


if __name__ == "__main__":
    main()
