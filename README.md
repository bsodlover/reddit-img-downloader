# reddit-img-downloader
This python script is going to download one or multiple subreddit's images along with it's thumbnail.
# Before running the script
You need to install urllib3. ```pip install urllib3```
# How to use
```python download_img_reddit.py url ```

The subreddit's url needs to be given in this format:

```https://www.reddit.com/r/subreddit.json?limit=number_of_desired_images```

For example, downloading 50 images from the subreddit t/wallpapers would be like this

``` python download_img_reddit.py https://www.reddit.com/r/wallpapers.json?limit=170 ```
