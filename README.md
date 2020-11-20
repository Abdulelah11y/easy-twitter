# Easy-Twitter
Simplifying Twitter APIs by leveraging tweepy APIs.

## Required steps
 1. Getting Twitter developer account. [For registration](https://developer.twitter.com/en/apply-for-access)
 2. Install Pandas package.
 3. Install Numpy package.
 4. Install Tweepy package.

```bash
# packages installation "In terminal"
conda install pandas
conda install numpy
pip install tweepy
```
```python
# importing packages in your jupyter notebook
import pandas as pd		# Please use the abbreviation "pd"
import numpy as np		# Please use the abbreviation "np"
import tweepy
```

## Installation
```bash
# how to install easytwitter package
pip install easytwitter
```

## Usage
- Import module

```python
# use * to access all the objects
from easytwitter import *
```

 - First your should establish the connection
```python
# returns 4 inputs to validate your twitter tokens.
user.connect_me()

# consumer_key = "xxxxxxxxxxxxxxxxxxxx"
# consumer_secret = "xxxxxxxxxxxxxxxxxxxxxxx"
# access_token = "xxxxxxxxxxxxxxxxxxxxxx"
# access_token_secret = "xxxxxxxxxxxxxxxxxxxxxxx"
```

## API Reference

### get_user_timeline()

Returns a summary of the latest 20 tweets of a specific twitter account.

``` python
# if you want to interact with the data, store it in a new dataframe
df = user.get_user_timeline()
df.head()
```

### get_followers_details()
Returns a users' followers details.

``` python
df = user.get_followers_details()
df.head()
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
