from instaPoster.twitter_poster import post_tweet
from instaPoster.generate import generate_img
from instaPoster.util import get_top
from instaPoster.instaSearcher import search_insta
from model.inference import infer

#search_insta("allblack")
#infer()
top_outfit = get_top()
generate_img(top_outfit)
post_tweet("Here is today's outfit of the day #ootd #kth #kthaisociety", "out_0.jpg")