import csv
import json

import filter

'''
Email a list of new job posts from Indeed. Applies filters to results.
'''

recent_scraped_jobs_path = './job_scraper/indeed.json'
post_list = []

# Copy the JSON from recently scraped jobs
with open(recent_scraped_jobs_path) as json_file:
    post_list = json.load(json_file)

# apply filters to posts
post_list = filter.apply_filters(post_list)
# print(post_list)


# construct email
