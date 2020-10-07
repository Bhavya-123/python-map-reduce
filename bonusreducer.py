# Bonus - Reducer using Files
# Easy to test
# Not quite Hadoop-ready

with open("sorter_bonus.txt","r") as sorted:
  with open("recucer_bonus.txt", "w") as output:

    thisKey = 0.0
    thisValue = ""

    for line in sorted:
      datalist = line.strip().split('\t')
      if (len(datalist) == 2) : 
        amount, paymentType = datalist

        if amount != thisKey:
          if thisKey:
            # output the previous key-summaryvalue result
            output.write(str(thisKey) + '\t' + thisValue+'\n')
            print(str(thisKey) + '\t' + thisValue+'\n')

          # start over for each new key
          thisKey = 0.0 
          thisValue = paymentType
  
        # apply the aggregation function
        thisKey += float(amount)

    # output the final key-summaryvalue result outside the loop
    output.write(str(thisKey) + '\t' + thisValue+'\n')
    print(str(thisKey) + '\t' + thisValue+'\n')
