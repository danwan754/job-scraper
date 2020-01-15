#!/bin/sh

# This script is run by windows task scheduler. The commands below are necessary inorder to successfully scrape Indeed.com and email new job postings.

cd /mnt/c/Users/Dan/Projects/python-projs/web-scrapers/job-scraper/job_scraper
source ../../venv/bin/activate
rm -f indeed.json
scrapy crawl indeed -o indeed.json
python run.py
