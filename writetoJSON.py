import json

#writes the inputs passed to a JSON file
def writetoJSON(path,fileName,data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data,fp)



#Code that calls writetoJSON
#path = './'             # specify the path to the directory you want the JSON file to be stored. ./ = current dir
#fileName = 'example'   # name of JSON file is example
#data = {}               # {} denotes a dictionary object - these are very to use for storing info into a JSON file
#data['cat'] = 'Vibe'
#data['val'] = 'Bouncy'
#writetoJSON(path, fileName, data)  # calling the function and passing the now-defined parameters path, fileName&data