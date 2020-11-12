# Easy-Twitter 
Simplifing Twitter APIs.

## How to use:
#### prerequisite

 - Twitter developer account. [For registration](https://developer.twitter.com/en/apply-for-access)
 - Install Easy-Twitter Package.
 
## Installation
```
pip install easytwitter
```

## Import
import all the functions
```
from easytwitter import *
```
import a specific function
```
from easytwitter import get_user_timeline()
```

## get_user_timeline() function
Call `get_user_timeline()` to retrieve the timeline of any twitter account. The default is set to 20 tweets. This function returns the tweets as a dataframe.

``` 
# To interact with the dataframe you should store the returned value in a new variable.

df = get_user_timeline()
df.head()
```