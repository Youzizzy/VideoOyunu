import json

def get_from_json(fileName):
    try:
        myJsonFile = open(fileName)
        myJsonTable = myJsonFile.read()
        pythonTable = json.loads(myJsonTable)
        myJsonFile.close()
        return pythonTable
    except:
        print("Must create file first")


def write_to_json(fileName, newTable):
    myJsonFile = open(fileName, "w")
    jsonTable = json.dumps(newTable, indent=2)
    myJsonFile.write(jsonTable)
    myJsonFile.close()
