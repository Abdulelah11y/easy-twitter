# Easy-Twitter
Simplifying Twitter APIs by leveraging tweepy library

## Prerequisites
 1. Twitter developer account. [For registration](https://developer.twitter.com/en/apply-for-access)
 2. Pandas library
```bash
# terminal
pip install pandas
```
```python
# python
import pandas
```
 3. Tweepy library
 ```bash
 # terminal
pip install tweepy
```
```python
# python
import tweepy
```

## Installation
```bash
# terminal
pip install easytwitter
```

## Usage
- Import module

```python
# to access all the functions
from easytwitter import *
```

 - First establish the connection
```python
# you need to enter your twitter tokens

# consumer_key = "xxxxxxxxxxxxxxxxxxxx"
# consumer_secret = "xxxxxxxxxxxxxxxxxxxxxxx"
# access_token = "xxxxxxxxxxxxxxxxxxxxxx"
# access_token_secret = "xxxxxxxxxxxxxxxxxxxxxxx"

user.connect_me()
```

## API Reference

### get_user_timeline()

Returns the 20 most recent statuses posted from the specified user as a dataframe. To interact with the dataframe, you should store the returned value.

``` python
df = user.get_user_timeline()
df.head()
```

### get_followers_details()

Returns a user’s followers details as a dataframe.

``` python
df = user.get_followers_details()
df.head()
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
