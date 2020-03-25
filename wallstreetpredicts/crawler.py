import json
from typing import List

import praw


def get_env_data():
    with open('.env') as f:
        data = json.load(f)
    return data['client-id'], data['client-secret'], data['username'], data['password']


def _get_instance() -> praw.Reddit:
    client_id, client_secret, username, password = get_env_data()
    return praw.Reddit(user_agent='WallStreetPredicts data collection',
                       client_id=client_id, client_secret=client_secret,
                       username=username, password=password)


def _comments_on_submission(submission: praw.models.Submission, replace_lim: int = 0) -> List[str]:
    print(f' *\tParsing comments with replace limit={replace_lim} on post: {submission.title}')
    submission.comments.replace_more(limit=replace_lim)
    return [comment.body for comment in submission.comments.list()]


def main():
    reddit = _get_instance()
    subreddit = reddit.subreddit('WallStreetBets')

    hot = subreddit.hot(limit=1)
    comments = []
    for submission in hot:
        comments.extend(_comments_on_submission(submission))

    print(len(comments))
    print(comments)


if __name__ == '__main__':
    main()
