# print("First module's name : {}".format(__name__))  #Output __main__

# Whenever Python runs a file it sets a few special variables and name is one of those.
# When python runs a file directly it sets the name variable to __main__



def main():
    print("First module's name : {}".format(__name__))  # Output __main__

if __name__=='__main__':
    main()


#If the value of __name__ ==__main__ it implies file is run directly
#If the value of __name__ not ==__main__ it implies imported file is run

