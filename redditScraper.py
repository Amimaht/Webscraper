import praw
import pandas as pd

reddit = praw.Reddit(client_id='###', client_secret='####', redirect_uri='http://localhost:8080', user_agent='webscrapping')

posts=[]
hot_posts= reddit.subreddit('pennystocks')

for post in hot_posts.new(limit=5) :
    posts.append([post.title, post.url])

posts = pd.DataFrame(posts, columns= ['title', 'url'])
print(posts)
