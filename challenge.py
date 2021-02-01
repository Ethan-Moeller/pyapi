import json

def main():

    with open("challenge.json","r") as vfile:
        datadictionary = vfile.read()
    
    datadecode = json.loads(datadictionary)

    print("name: ", datadecode[3]['name'])
    print("eye color: ", datadecode[3]['eyeColor'])
    print("favorite fruit", datadecode[3]['favoriteFruit'])

if __name__ == "__main__":
    main()
