import json

#writes the inputs passed to a JSON file
def readfromJSON(path,fileName):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'r') as fp:
        info = json.load(fp)
    return(info)




#path = './'  # specify the path to the directory you want the JSON file to be stored. ./ = current directory
#fileName = 'example'  # name of JSON file is example
#print(readfromJSON(path, fileName))  # calling the function and passing the now-defined parameters path, fileName&data