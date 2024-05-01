import pandas as pd

logo= '''
          _____                    _____                    _____          
         /\    \                  /\    \                  /\    \         
        /::\    \                /::\    \                /::\    \        
       /::::\    \              /::::\    \              /::::\    \       
      /::::::\    \            /::::::\    \            /::::::\    \      
     /:::/\:::\    \          /:::/\:::\    \          /:::/\:::\    \     
    /:::/__\:::\    \        /:::/__\:::\    \        /:::/__\:::\    \    
   /::::\   \:::\    \      /::::\   \:::\    \       \:::\   \:::\    \   
  /::::::\   \:::\    \    /::::::\   \:::\    \    ___\:::\   \:::\    \  
 /:::/\:::\   \:::\____\  /:::/\:::\   \:::\    \  /\   \:::\   \:::\    \ 
/:::/  \:::\   \:::|    |/:::/__\:::\   \:::\____\/::\   \:::\   \:::\____\
\::/   |::::\  /:::|____|\:::\   \:::\   \::/    /\:::\   \:::\   \::/    /
 \/____|:::::\/:::/    /  \:::\   \:::\   \/____/  \:::\   \:::\   \/____/ 
       |:::::::::/    /    \:::\   \:::\    \       \:::\   \:::\    \     
       |::|\::::/    /      \:::\   \:::\____\       \:::\   \:::\____\    
       |::| \::/____/        \:::\   \::/    /        \:::\  /:::/    /    
       |::|  ~|               \:::\   \/____/          \:::\/:::/    /     
       |::|   |                \:::\    \               \::::::/    /      
       \::|   |                 \:::\____\               \::::/    /       
        \:|   |                  \::/    /                \::/    /        
         \|___|                   \/____/                  \/____/         
                                                                           
'''
print(logo)

def compare_csv(file1, file2):
    print('Reading Fle 1')
    # Read both CSV files into pandas DataFrames
    df1 = pd.read_csv(file1)
    print('Reading File 2')
    df2 = pd.read_csv(file2)

    # Compare DataFrames
    differences = []

    print('Analysing The Differences')
    # Iterate over each row in both DataFrames
    for index, row in df1.iterrows():
        for col in df1.columns:
            # Check if the values in corresponding cells are different
            if row[col] != df2.at[index, col]:
                differences.append(f"In S.No {index+1}, {col} has been changed from {row[col]} to {df2.at[index, col]}")

    return differences

file1 = "battery1.csv"
file2 = "battery2.csv"

differences = compare_csv(file1, file2)

if differences:
    print("Differences found:")
    for diff in differences:
        print(diff)
else:
    print("No differences found.")
