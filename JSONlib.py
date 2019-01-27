import json

def readfromJSON(path):     #reads the information stored in a JSON file
    filePath= path
    with open(filePath, 'r') as fp:
        info = json.load(fp)
    return(info)


def writetoJSON(path,data):     #writes the inputs passed to a JSON file
    filePath = path
    with open(filePath, 'w') as fp:
        json.dump(data,fp)

#def newJSON(directory):


def keyDeleteJSON(filepath, key):
    dict = readfromJSON(filepath)
    try:
        del dict[key]
    except KeyError:
        print(key, ' key not found')
    return dict

#def valDeleteJSON


def getTagsfromJSON(filepath):  #returns the dictionary from the JSON file without the Filepath key:value
    return keyDeleteJSON(filepath,"Filepath")

    #dict = readfromJSON(filepath)
    #try:
    #    del dict["Filepath"]
    #except KeyError:
    #    print('"Filename" key not found')
    #return dict



#Code that calls writetoJSON
#path = './'             # specify the path to the directory you want the JSON file to be stored. ./ = current dir
#fileName = 'example'   # name of JSON file is example
#data = {}               # {} denotes a dictionary object - these are very to use for storing info into a JSON file
#data['cat'] = 'Vibe'
#data['val'] = 'Bouncy'
#writetoJSON(path, fileName, data)  # calling the function and passing the now-defined parameters path, fileName&data

path = 'C:\\Users\\Shahaan\\Documents\\DeltahacksPR\\jsonfiletemplate.json'

print(readfromJSON(path))
print(getTagsfromJSON(path))