import json


def processing(file):
    res = []
    for k in file:
        ex = k[0] + ": " + str(k[1])
        res.append(ex)
    return res


def generate_diff(path_file1, path_file2):
    file1 = json.load(open(path_file1))
    file2 = json.load(open(path_file2))
    all = list(set(file1.items()) | set(file2.items()))
    all.sort(key=lambda key: key[0])
    all = processing(all)
    common = file1.items() & file2.items()
    common = processing(common)
    unique1 = file1.items() - file2.items()
    unique1 = processing(unique1)
    unique2 = file2.items() - file1.items()
    unique2 = processing(unique2)
    result = ''
    for k in all:
        if k in common:
            result +=  '   ' + k + '\n'
        elif k in unique1:
            result +=  ' - ' + k + '\n'
        elif k in unique2:
            result +=  ' + ' + k + '\n'
    result = '{\n' + result + '}'
    print (result)
    return result
        
generate_diff('gendiff/files/file1.json', 'gendiff/files/file2.json')