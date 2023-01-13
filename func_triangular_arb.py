# Structure trading pair groups
def structure_trading_pairs(pairs):

    triangular_pairs_list = []
    remove_duplicates_list = []
    pairs_list = pairs[0:20]

    # Loop through each coin to find potential matches
    for pair_a in pairs_list:

        # Get pair A
        a_base = pair_a["token0"]["symbol"]
        a_quote = pair_a["token1"]["symbol"]
        a_pair = a_base + "_" + a_quote
        a_token_0_id = pair_a["token0"]["id"]
        a_token_1_id = pair_a["token1"]["id"]
        a_contract = pair_a["id"]
        a_token_0_decimals = pair_a["token0"]["decimals"]
        a_token_1_decimals = pair_a["token1"]["decimals"]
        a_token_0_price = pair_a["token0Price"]
        a_token_1_price = pair_a["token1Price"]

        # Put A into a box for checking at B
        a_pair_box = [a_base, a_quote]

        for pair_b in pairs_list:

            # Get pair B
            b_base = pair_b["token0"]["symbol"]
            b_quote = pair_b["token1"]["symbol"]
            b_pair = b_base + "_" + b_quote
            b_token_0_id = pair_b["token0"]["id"]
            b_token_1_id = pair_b["token1"]["id"]
            b_contract = pair_b["id"]
            b_token_0_decimals = pair_b["token0"]["decimals"]
            b_token_1_decimals = pair_b["token1"]["decimals"]
            b_token_0_price = pair_b["token0Price"]
            b_token_1_price = pair_b["token1Price"]

            # Get Pair C
            if a_pair != b_pair:
                if b_base in a_pair_box or b_quote in a_pair_box:

                    for pair_c in pairs_list:

                        c_base = pair_c["token0"]["symbol"]
                        c_quote = pair_c["token1"]["symbol"]
                        c_pair = c_base + "_" + c_quote
                        c_token_0_id = pair_c["token0"]["id"]
                        c_token_1_id = pair_c["token1"]["id"]
                        c_contract = pair_c["id"]
                        c_token_0_decimals = pair_c["token0"]["decimals"]
                        c_token_1_decimals = pair_c["token1"]["decimals"]
                        c_token_0_price = pair_c["token0Price"]
                        c_token_1_price = pair_c["token1Price"]

                        # Count number of C items
                        if c_pair != a_pair and c_pair != b_pair:
                            combine_all = [a_pair, b_pair, c_pair]
                            pair_box = [a_base, a_quote, b_base, b_quote, c_base, c_quote]

                            counts_c_base = 0
                            for i in pair_box:
                                if i == c_base:
                                    counts_c_base += 1

                            counts_c_quote = 0
                            for i in pair_box:
                                if i == c_quote:
                                    counts_c_quote += 1

                            if counts_c_base == 2 and counts_c_quote == 2 and c_base != c_quote:
                                combined = a_pair + "," + b_pair + "," + c_pair
                                unique_string = ''.join(sorted(combined))