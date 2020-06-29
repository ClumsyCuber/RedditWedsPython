import praw
reddit = praw.Reddit(client_id="for client id, vist reddit.com/prefs/apps",
                         client_secret="same as id", password="reddit account password",
                         user_agent="HiddenFilter(can be anything)", username="reddit account username")
                      
for submission in reddit.subreddit('BrawlStars').hot(limit=1):
	print(submission.title)
 for submission in reddit.user.me().hidden(limit=1):
	submission.unsave
for submission in reddit.user.me().hidden(limit=1):
	if submission.subreddit == "BrawlStarsP":
		print("lmao, you freak!")
for submission in reddit.user.me().hidden(limit=None):
	if submission.subreddit not in list_of_subs:
		list_of_subs.append(submission.subreddit)
        
