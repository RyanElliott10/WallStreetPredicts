import json
import praw
import sys


def get_env_data():
    with open('.env') as f:
        data = json.load(f)
    return data['client-id'], data['client-secret'], data['username'], data['password']


def main():
    client_id, client_secret, username, password = get_env_data()
    reddit = praw.Reddit(user_agent='WallStreetPredicts data collection',
                         client_id=client_id, client_secret=client_secret,
                         username=username, password=password)
    subreddit = reddit.subreddit('wallstreetbets')

    hot = subreddit.hot(limit=10)
    comments = []
    for submission in hot:
        print(submission.title)
        comments = submission.comments
        for comment in comments:
            try:
                comments.append(comment.body)
            except:
                try:
                    more_comments = comment.comments
                    print('\n\n\n\n\n\nMORE COMMENTS\n:', more_comments)
                except:
                    print('neither')


if __name__ == '__main__':
    main()
