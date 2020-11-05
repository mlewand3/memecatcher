## memecatcher

To see site in full glory, please visit:

www.memecatcher.herokuapp.com

Simple script for taking memes from various sites and wrapped in flask app.

No ads, no buttons, no additional links, no stupid headers taking
1/3 of screen, no logging, no comments - only pure fun.

## How it works?

Implementation is naive.
When app is asked to generate page number *2* of memes, chosen sites is 
scrapped from page *2* of its content, and then merged together on one screen.
Script is heavyly using BeautifulSoup and request library.
App layer uses flask, and bootstrap.

## Disclaimer

This is script for personal-use only (and made purely for fun),
I do not to use recommend it other way.
Please remember that most of these memes are owned by these sites.

## Developing

To start developing, please create new virtual enviroment
and install requirements:

```
pip install -r requirements.txt
pip install -r requirements.dev.txt
```

And following command to start app:

```
python run.py
```

And then visit localhost:5000 in your browser.
