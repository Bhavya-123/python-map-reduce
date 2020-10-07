# Bonus- Mapper using Files
# Easy to test
# Not quite Hadoop-ready

# open returns a file object
with open("mappedbypaymenttype.txt", "r") as input:
  with open("mapper_bonus.txt", "w") as output:

    # iterate through each line in the file object
    for line in input:
      datalist = line.strip().split("\t")
      if (len(datalist) == 2) : 
        paymentType, amount = datalist

        # output intermediate key-value pairs
        output.write(amount + "\t" + paymentType + "\n")

        # display to console (not required - just for the user)
        print(amount + "\t" + paymentType + "\n")

