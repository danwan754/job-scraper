import os
import csv


def apply_filters(posts):
    '''
    Parameters:
        posts: A list of dictionaries representing a job post
    Returns the remaining list of dictionaries after filters are applied.
    '''

    history_ids_path = './indeed_ids_history.csv'
    exclude_criteria_path = './exclude.csv'

    # if history of IDs file does not exist, create it
    if not os.path.isfile(history_ids_path):
        with open(history_ids_path, 'w'):
            pass

    # if exclusion file does not exist, create it
    if not os.path.isfile(exclude_criteria_path):
        with open(exclude_criteria_path, 'w'):
            pass    

    posts = exclude_seen(posts, history_ids_path)
    posts = exclude_companies(posts, exclude_criteria_path)

    # print(posts)
    return posts


def exclude_seen(posts, history_ids_path):
    '''
    Parameters:
        posts: A list of dictionaries representing a job post.
        recent_jobs_file_path: File path to JSON file containing recently scraped job posts.
        history_ids_path: File path to CSV file containing previously seen job IDs.
    Returns the remaining list of dictionaries in 'posts' after posts with seen IDs are removed.
    '''

    # job post not seen yet
    post_list = []

    # job post IDs seen in history
    seen_ids = []

    # copy the post IDs in csv file to seen_ids list
    with open(history_ids_path, newline='') as csvfile:
        fileReader = csv.reader(csvfile, delimiter=' ')
        for row in fileReader:
            seen_ids.append(row[0])

    for post in posts:
        # post_ids.append(post['id'])
        if (post['id'] not in seen_ids):
            post_list.append(post)

    return post_list


def exclude_companies(posts, file_path):
    '''
    Parameters:
        posts: A list of dictionaries representing a job post.
        file_path: File path to csv file containing names of companies to exclude.
    Returns the remaining list of dictionaries after removing posts from excluded companies.
    '''

    # list of company names to filter out
    names = []

    # copy the company names from csv file
    with open(file_path, 'r') as csv_file:
        fileReader = csv.reader(csv_file, delimiter=' ')
        for row in fileReader:
            names.append(row[0].lower())
    
    return [i for i in posts if i['company'].lower() not in names]




