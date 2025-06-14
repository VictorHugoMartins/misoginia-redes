import re

execution = 'local'
# execution = 'cloud'

base_path = 'data' if execution == 'local' else 'cloud'
country = 'palestine'

# unused
# Para voltar a usar, pesquise por "# Verifica se o título possui as palavras chave" e descomente a condição
key_words = [] 

data = { # unused
    "country": (),
    "complement": (),
    "source": ()
}

templates = ["[country] [complement]"]

def extract_variables(string):
    regex = r"\[(\w+)\]"
    variables = re.findall(regex, string)
    return variables

def generate_single_template(template, data):
    temp = [template]
    temp_2 = []
    n = len(extract_variables(template))

    for element in data:
        for string in temp:
            for value in data[element]:
                temp_2.append(string.replace(f"[{element}]", value))

        for item in temp_2:
            temp.append(item)
        for item in temp:
            if len(extract_variables(item)) == n:
                temp.remove(item)
                n -= 1
        temp_2 = []

    res = []
    for item in temp:
        if len(extract_variables(item)) == 0:
            res.append(item)
    return res

def generate_queries():
    queries = []
    for template in templates:
        template_data = {variable: data[variable] for variable in extract_variables(template)}
        queries.extend(generate_single_template(template, template_data))
    return queries