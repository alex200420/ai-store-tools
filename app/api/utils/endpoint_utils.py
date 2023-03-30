from typing import List
import numpy as np
import openai
from scipy import spatial
import re

# constants
EMBEDDING_MODEL = "text-embedding-ada-002"

#TBD Cache for embeddings
def closest_recommendations_from_strings(
    embeddings: List[np.array],
    database: np.array,
    query_strings: List[str],
    model=EMBEDDING_MODEL,
) -> List[int]:
    """Print out the k nearest neighbors of a given string."""
    indices_ls = []
    for query_string in query_strings:
        # get the embedding of the source string
        query_embedding = get_embedding(query_string, model)
        # get distances between the source embedding and other embeddings (function from embeddings_utils.py)
        distances = distances_from_embeddings(query_embedding, embeddings, distance_metric="cosine")
        # get indices of nearest neighbors (function from embeddings_utils.py)
        indices_of_nearest_neighbors = indices_of_nearest_neighbors_from_distances(distances)
        indices_ls.append(indices_of_nearest_neighbors[0])
    response = {"recommended_products": []}
    for idx in indices_ls:
        response['recommended_products'].append({
            'product_id': str(database[idx, 0]),
            'product_name': str(database[idx, 1]),
            'store_id': str(database[idx, 2]),
            'price': float(database[idx, 5])
        })
    return response

def parse_cpgs_recipe_input(recipe_string: str):
    #formatting suggested by chatgpt
    recipe_dict = {}
    clean_recipe_string = clean_gpt_response(recipe_string).replace("\n\n\n","\n")
    recipe_strings = clean_recipe_string.split('\n\n')

    for recipe in recipe_strings:
        recipe_lines = recipe.strip().split('\n')
        recipe_name = recipe_lines[0].strip()
        recipe_ingredients = [ingredient.strip()[1:].strip() for ingredient in recipe_lines[1:]]
        if len(recipe_name) > 0:
            recipe_dict[recipe_name] = recipe_ingredients
    
    return recipe_dict, clean_recipe_string

def parse_rest_input(unparsed_response: str):
    formatted_products = []
    product_names = []
    for line in unparsed_response.split('\n'):
        if '-' not in line:
            pass
        else:
            product_name = line.split('Product ID')[0].replace("..",".").replace("- ", "").strip()
            product_id, store_id = re.findall('\d+', line)[:2]

            # Create a dictionary to hold the formatted product information
            formatted_product = {
                "product_id": product_id,
                "product_name": product_name,
                "store_id": store_id
            }
            
            # Add the formatted product to the list of formatted products
            formatted_products.append(formatted_product)
            product_names.append(product_name)  

    # Create a dictionary to hold the formatted product information
    message = "Te recomendamos los siguientes productos!\n- {}".format("\n- ".join(product_names))
    output_dict = {
        "recommended_products": formatted_products,
        "message": message
    }
    return output_dict

def get_embedding(text: str, engine="text-similarity-davinci-001") -> List[float]:

    # replace newlines, which can negatively affect performance.
    text = text.replace("\n", " ")

    return openai.Embedding.create(input=[text], engine=engine)["data"][0]["embedding"]

def distances_from_embeddings(
    query_embedding: List[float],
    embeddings: List[List[float]],
    distance_metric="cosine",
) -> List[List]:
    """Return the distances between a query embedding and a list of embeddings."""
    distance_metrics = {
        "cosine": spatial.distance.cosine,
        "L1": spatial.distance.cityblock,
        "L2": spatial.distance.euclidean,
        "Linf": spatial.distance.chebyshev,
    }
    distances = [
        distance_metrics[distance_metric](query_embedding, embedding)
        for embedding in embeddings
    ]
    return distances


def indices_of_nearest_neighbors_from_distances(distances) -> np.ndarray:
    """Return a list of indices of nearest neighbors from a list of distances."""
    return np.argsort(distances)

def clean_gpt_response(response: str):
    return response.replace("\n\n\n","\n").replace("\n", "\n\n").replace(": ", ":\n- ").replace(",", "\n-").replace("\n\n-", "\n-")