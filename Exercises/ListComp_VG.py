#######################################################
# List Comprehension Exercises
# Duty-1
# Import of the Library
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("car_crashes")
# The first five lines of the data column
df.head()
# Indexes of the data set
df.columns


["NUM_"+ deger.upper() if df[deger].dtype != "O" else deger.upper() for deger in df.columns]

# b = ["NUM_" + i.upper() if df[i].dtypes == float else i.upper() for i in df]

#Duty-2
# Import of the Library
import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

[deger.upper() +"_FLAG" if "no" not in deger else deger.upper() for deger in df.columns]


#Duty-3
# Import of the Library
import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

of_list = ["abbrev", "no_previous"]

new_cols= [deger for deger in df.columns if deger not in  of_list]

new_df= df[new_cols]
new_df.head()