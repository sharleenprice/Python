"""
Created on Fri Oct 20 21:38:32 2017

@author: sharleen price spp2122

"""
def read_markets(filename):
    """
    Read in the farmers market data from the file named filename and return 
    a tuple of two objects:
    1) A dictionary mapping zip codes to lists of farmers market tuples.
    2) A dictionary mapping towns to sets of zip codes.
    """
    
    f = open(filename, "r")
    zipcode_to_market = {}
    town_to_zip = {}
    for line in f:
        fixedline =line.strip().split("#")
        temp_list  = fixedline[0:5]
        new_tup = tuple(temp_list)
        state, market_name, street_address, city, zipcode = new_tup
        
        if zipcode not in zipcode_to_market:
            zipcode_to_market[zipcode] = []
        zipcode_to_market[zipcode].append(new_tup)
    
        if city not in town_to_zip:
            town_to_zip[city] = set()
        town_to_zip[city].add(zipcode)
        
    return zipcode_to_market, town_to_zip

def print_market(market):
    """
    Returns a human-readable string representing the farmers market tuple
    passed to the market parameter.
    """
    state, market_name, street_address, city, zipcode = market
    
    return "\n {} \n {} \n {}, {} {}".format(market_name,street_address, city, state, zipcode ) # replace this line
    

if __name__ == "__main__":

    # This main program first reads in the markets.txt once (using the function
    # from part (a)), and then asks the user repeatedly to enter a zip code or
    # a town name (in a while loop until the user types "quit").

    FILENAME = "markets.txt"
    args = True

    try: 
        zip_to_market, town_to_zips = read_markets(FILENAME)
        while (args == True):
              user_input = input("Please enter a town or zipcode or type quit \n")
              try:
                  user_some= int(user_input)
                  try:
                      list_of_markets = zip_to_market[user_input]
                      for tups in range(0,len(list_of_markets)):
                          market_tup = list_of_markets[tups]
                          print(print_market(market_tup))
                  except KeyError:
                      print("Zipcode Not Found")
              except ValueError:
                  if user_input == "quit":
                      args = False
                  else:
                      try:
                          user_town_set = town_to_zips[user_input]
                          zips_as_list = list(user_town_set)
                          for zipcodes in zips_as_list:
                              list_in_zip= zip_to_market[zipcodes]
                              for tups in range(0, len(list_in_zip)):
                                  market_tup = list_in_zip[tups]
                                  print(print_market(market_tup))
                      except KeyError:
                            print("Town Not Found")
                              

    except (FileNotFoundError, IOError): 
        print("Error reading {}".format(FILENAME))
    

