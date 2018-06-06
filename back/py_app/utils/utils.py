def toJson(object):
    return object.to_json()

def convertParamToColumn(param):
    names_columns = {
        'country': '  PAIS  ',
        'personType': ' FISICA_JURIDICA ',
        'globalSegment': '         SEGMENTO_GLOBAL          '
    }
    list_result = []
    for element in param:
        if element:
            list_result.append(names_columns[element])

    return list_result
