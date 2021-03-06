###############################################################
############### RESOURCES
https://developers.google.com/edu/python/introduction
https://docs.python.org/3/tutorial/index.html


####################### GETTING STARTED

# FUNCTIONS AND LOOPS!!!

# 1: FUNCTIONS
    # Global Scope-available in main body of script. Call 'global' before the local variable.
    # Local Scope-available only in local function. Local is always searched first in a function
    # Built In Scope
    # Flexible Functions
    # Extract_data
    # Comprehensions (Like apply functions from R)
# 2: LOOPS
    # IF statement
    # FOR statement
    # RANGE statement
    # BREAK / CONTINUE / ELSE
    # Looping over Columns
    # MSE Loop
# 3: LAMBDA FUNCTIONS
# 4: COMMON FUNCTIONS

############################################################
#################### FUNCTIONS

# WRITING FUNCTIONS BASICS
def shout(word):
    """ Make the word concatenated with !!! """ # This is the definition of what the function does!
    shout_word = word + '!!!'
    print(shout_word)


# Define shout with parameters word1 and word2
def shout(word1, word2):
    """Concatenate strings with three exclamation marks"""
    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + '!!!'
    # Concatenate word2 with '!!!': shout2
    shout2 = word2 + '!!!'
    # Concatenate shout1 with shout2: new_shout
    new_shout = shout1 + shout2
    # Return new_shout
    return new_shout
# Pass 'congratulations' and 'you' to shout(): yell
yell = shout('congratulations','you')
print(yell)


# MORE COMPLICATED OF ABOVE : Define shout_all with parameters word1 and word2
def shout_all(word1, word2):
    # Concatenate word1 with '!!!': shout1
    shout1 = word1 + '!!!'
    # Concatenate word2 with '!!!': shout2
    shout2 = word2 + '!!!'
    # Construct a tuple with shout1 and shout2: shout_words
    shout_words = (shout1, shout2)
    # Return shout_words
    return shout_words
# Pass 'congratulations' and 'you' to shout_all(): yell1, yell2
yell1, yell2 = (shout_all('congratulations','you'))
# Print yell1 and yell2
print(yell1)
print(yell2)


# NESTED FUNCTION

# Define three_shouts
def three_shouts(word1, word2, word3):
    """Returns a tuple of strings
    concatenated with '!!!'."""
    # Define inner
    def inner(word):
        """Returns a string concatenated with '!!!'."""
        return word + '!!!'
    # Return a tuple of strings
    return (inner(word1), inner(word2), inner(word3))
# Call three_shouts() and print
print(three_shouts('a', 'b', 'c'))


# FLEXIBLE ARGs

# 1
# Define shout_echo
def shout_echo(word1, echo=1, intense=False):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""
    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo
    # Capitalize echo_word if intense is True
    if intense is True:
        # Capitalize and concatenate '!!!': echo_word_new
        echo_word_new = echo_word.upper() + '!!!'
    else:
        # Concatenate '!!!' to echo_word: echo_word_new
        echo_word_new = echo_word + '!!!'
    # Return echo_word_new
    return echo_word_new

# Call shout_echo() with "Hey", echo=5 and intense=True: with_big_echo
with_big_echo = shout_echo('Hey', 5, True)

# 2 - Multi ARGs (*args) and (**kwargs)
# Define report_status
def report_status(**kwargs):
    """Print out the status of a movie character."""
    print("\nBEGIN: REPORT\n")
    # Iterate over the key-value pairs of kwargs
    for keys, values in kwargs.items():
        # Print out the keys and values, separated by a colon ':'
        print(keys + ": " + values)
    print("\nEND REPORT")

# First call to report_status()
report_status(name = 'luke', affiliation = 'jedi', status = 'missing')
# Second call to report_status()
report_status(name='anakin', affiliation='sith lord', status='deceased')



# EXTRACT_DATA (filename, num_images)

def extract_data(filename, num_images):
    with gzip.open(filename) as bytestream:
        bytestream.read(16)
        buf = bytestream.read(28 * 28 * num_images)
        data = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
        data = data.reshape(num_images, 28,28)
        return data
train_data = extract_data('train-images-idx3-ubyte.gz', 60000)
test_data = extract_data('t10k-images-idx3-ubyte.gz', 10000)

# EXTRACT_LABELS (filename, num_images)

def extract_labels(filename, num_images):
    with gzip.open(filename) as bytestream:
        bytestream.read(8)
        buf = bytestream.read(1 * num_images)
        labels = np.frombuffer(buf, dtype=np.uint8).astype(np.int64)
        return labels
train_labels = extract_labels('train-labels-idx1-ubyte.gz',60000)
test_labels = extract_labels('t10k-labels-idx1-ubyte.gz',10000)


# COMPREHENSIONS (List & Dictionary Comprehensions): Like apply functions in R
# R has apply(); Py has map()
# map the binge_female function to num_drinks
print(list(map(binge_female, num_drinks))) # map(x,y) applys function x to y variable but returns a map object so we must list()

# Ex.
# Append dataframes into list with for loop
dfs_list = []
for f in inflam_files:
    dat = pd.read_csv(f)
    dfs_list.append(dat)
# Re-write the provided for loop as a list comprehension: dfs_comp
dfs_comp = [pd.read_csv(f) for f in inflam_files]
print(dfs_comp)

# EX.
[['jonathan', 458], ['daniel', 660], ['hugo', 3509], ['datacamp', 26400]]
# Write a dict comprehension
tf_dict = {key:value for key,value in twitter_followers}



############################################################
#################### LOOPS

# IF STATEMENTS

x = int(input("Please enter an integer: "))
Please enter an integer: 42

if x < 0:
     x = 0
     print('Negative changed to zero')
 elif x == 0:
     print('Zero')
 elif x == 1:
     print('Single')
 else:
     print('More')

num_drinks = 5
# if statement
if num_drinks < 0:
    print('error')
# elif statement
elif num_drinks <= 4:
    print('non-binge')
# else statement
else:
    print('binge')

num_drinks = [5, 4, 3, 3, 3, 5, 6, 10]
# Write a for loop
for drink in num_drinks:
    # if/else statement
    if drink <= 4:
        print('non-binge')
    else:
        print('binge')


# FOR LOOPS

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
cat 3
window 6
defenestrate 12

for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)
['defenestrate', 'cat', 'window', 'defenestrate']

# Create the empty list: baby_names
baby_names = []
# Loop over records 
for row in records:
    # Add the name to the list
    baby_names.append(row[3])
# Sort the names in alphabetical order
for name in sorted(baby_names):
    # Print each name
    print(name)

# RANGE STATEMENT

for i in range(5):
    print(i)
0
1
2
3
4

range(5, 10)
   5, 6, 7, 8, 9

range(0, 10, 3)
   0, 3, 6, 9

range(-10, -100, -30)
  -10, -40, -70

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
     print(i, a[i])
0 Mary
1 had
2 a
3 little
4 lamb


# BREAK / CONTINUE & ELSE STATEMENTS

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # Loop feel through without finding a factor
        print(n, 'is a prime number')
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3

for num in range(2, 10):
     if num % 2 == 0:
         print("Found an even number", num)
         continue
     print("Found a number", num)
Found an even number 2
Found a number 3
Found an even number 4
Found a number 5
Found an even number 6
Found a number 7
Found an even number 8
Found a number 9



# 1: Looping over items in a column and counting how many languages there are in the tweets data
import pandas as pd
# Import Twitter data as DataFrame: df
df = pd.read_csv('tweets.csv')
# Initialize an empty dictionary: langs_count
langs_count = {}
# Extract column from DataFrame: col
col = df['lang']
# Iterate over lang column in DataFrame
for entry in col:
    # If the language is in langs_count, add 1
    if entry in langs_count.keys():
        langs_count[entry] += 1
    # Else add the language to langs_count, set the value to 1
    else:
        langs_count[entry] = 1
# Print the populated dictionary
print(langs_count)
 {'en': 97, 'und': 2, 'et': 1}

# 2: MSE LOOP
n_updates = 20
mse_hist = []
# Iterate over the number of updates
for i in range(n_updates):
    # Calculate the slope: slope
    slope = get_slope(input_data, target, weights)
    # Update the weights: weights
    weights = weights - (0.01 * slope)
    # Calculate mse with new weights: mse
    mse = get_mse(input_data, target, weights)
    # Append the mse to mse_hist
    mse_hist.append(mse)

# Plot the mse history
plt.plot(mse_hist)
plt.xlabel('Iterations')
plt.ylabel('Mean Squared Error')
plt.show()


############################################################
#################### LAMBDA FUNCTIONS

raise_to_power = lambda x, y: x ** y

echo_word = lambda word1, echo: word1 * echo
echo_word('word', 4)

# Create a list of strings: spells
spells = ["protego", "accio", "expecto patronum", "legilimens"]
# Use map() to apply a lambda function over spells: shout_spells
shout_spells = map(lambda a: a + '!!!', spells) # Map converts to map item-- use list to show it
# Convert shout_spells to a list: shout_spells_list
shout_spells_list = list(shout_spells)
# Convert shout_spells into a list and print it
print(shout_spells_list)

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
# Use filter() to apply a lambda function over fellowship: result
result = filter(lambda a: len(a) > 6, fellowship)
# Convert result to a list: result_list
result_list = list(result)
# Convert result into a list and print it
print(result_list)





############################################################
#################### COMMON FUNCTIONS

dict() # turns something into a dictionary instead of x={} method

sorted( , reverse = True)

print(df.get(105, 'Not Found')) # Searches for 105 as the KEY and prints the value, otherwise prints "not found"

pop() # pops key values out of dictionaries

.strip() # Removes leading and lagging whitespace using the string accessor
df['name_strip'] = df['name'].str.strip()