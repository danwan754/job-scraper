import csv
import json

import filter
import email_sender

'''
Email a list of new job posts from Indeed. Applies filters to results.
'''

recent_scraped_jobs_path = './indeed.json'
history_ids_path = './indeed_ids_history.csv'
post_list = []

# load the JSON from recently scraped jobs
with open(recent_scraped_jobs_path) as json_file:
    post_list = json.load(json_file)

# apply filters to posts
post_list = filter.apply_filters(post_list)

# load email config
config_dict = {}
config_file_path = './config.json'
with open(config_file_path, 'r') as json_file:
    config_dict = json.load(json_file)

# send email
email_sender.send_email(config_dict, post_list)

# update post ID history with IDs of posts that were just emailed out
with open(history_ids_path, 'a') as csv_file:
    writer = csv.writer(csv_file, delimiter=' ')
    rows_of_post_ids = [[post['id']] for post in post_list]
    writer.writerows(rows_of_post_ids)

