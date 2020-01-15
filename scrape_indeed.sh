#!/bin/sh

# This script is run by windows task scheduler. The commands below are necessary inorder to scrape and email new job postings.

cd <full project path>
source ./venv/bin/activate
rm -f indeed.json
scrapy crawl indeed -o indeed.json
python run.py
