
import json



def load_json(data_file):
    """ """

    # load data
    with open(data_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data

    



if __name__ == "__main__":


    data_file = "data/toy.json"

    load_json(data_file)

    
