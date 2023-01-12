# https://thegraph.com/hosted-service/subgraph/uniswap/uniswap-v3

import requests
import json

""" Retrive Graph QL mid prices for uniswap """

def retrieve_uniswap_information():

    query = """
        {
            pools (orderBy: totalValueLockedETH, orderDirection: desc, first: 500) {
                id
                totalValueLockedETH
                token0Price
                token1Price
                feeTier
                token0 {id symbol name decimals}
                token1 {id symbol name decimals}
            }
        }
    """

    url = "https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3"
    req = requests.post(url, json={'query': query})
    json_dict = json.loads(req.text)
    return json_dict

if __name__ == "__main__":
    mid_prices = retrieve_uniswap_information()
    print(mid_prices["data"]["pools"][0:3])