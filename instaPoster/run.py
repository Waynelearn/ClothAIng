from twitter_poster import post_tweet
from generate import generate_img
from util import get_top

top_outfit = get_top()
generate_img(top_outfit)
post_tweet("Here is today's outfit of the day #ootd #kth #kthaisociety", "out_0.jpg")