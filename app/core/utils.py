
import yaml 

class YAML_Handler():
    """
    A class that provides methods for working with YAML files.

    :param path: A string representing the path to the YAML file.
    """
    def __init__(self, path:str):
        self.path = path
        self.YAML_DICT = self.load_yaml_file(path)

    def load_yaml_file(self, path:str) -> dict:
        """
        Loads a YAML object from a file.

        :param path: A string representing the path to the YAML file.
        :return: A dictionary representing the contents of the YAML file.
        """
        with open(path, mode='rt',encoding='UTF-8') as file:
            try:
                variables = yaml.safe_load(file)
            except yaml.YAMLError as exc:
                #log exception
                print(exc)
        return variables

    def get_yaml_unpacked(self, key:str):
        """
        Returns a YAML dictionary unpacked into a class with attributes that can be accessed using attribute notation.

        :param yaml_dict: A YAML dictionary.
        :param key: A string representing the key to retrieve from the dictionary.
        :return: A class instance with attributes for each key-value pair in the dictionary.
        """
        dict_key = self.YAML_DICT[key]

        class recursive_attribute_dict:
            """
            A class that allows accessing nested dictionaries using attribute notation.
            """
            def __init__(self, dictionary):
                for key, value in dictionary.items():
                    if isinstance(value, dict):
                        setattr(self, key, recursive_attribute_dict(value))
                    else:
                        setattr(self, key, value)

            def __getitem__(self, key):
                return getattr(self, key)
                
        return recursive_attribute_dict(dict_key)