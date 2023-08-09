# For all numbers between 1 and 1000, find the ones which are divisible by 7 
# but are not a multiple of 5 and also divisible by 13.
# Then concatenate them into a string separated by ‘_’. 
# Prepend this string to ‘@trackview.io’ and send your CV to the address (e.g., 1_2_3_4@compnay.io).
# ---------------

# Define resultArray as empty
# For all numbers between 1 and 1000
#     find the ones which are divisible by 7
#         but are not a multiple of 5 and also divisible by 13.
#             Add the numbers we get to resultArray
# Covert int array to string array
# Then concatenate resultArray into a string separated by ‘_’
# Prepend this string to ‘@company.io’

resultArray = []
for x in range(7, 1001, 7):
    if x%5 and not x%13:
        resultArray.append(str(x))
email = "_".join(resultArray) + "@company.io"
print(email)