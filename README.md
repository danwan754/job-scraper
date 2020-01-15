# Job Scraper
Scrape job ads, filter, and email results.

This application will scrape the most recent developer job postings on Indeed.com. It can filter out any companies you do not want to see. The resulting job postings will be emailed to you. You should look through all postings listed in your emails as the same posts will never be emailed again (unless the employer create a new posting for the same position).

I wrote this application for my personal use to find developer jobs in Vancouver, BC. It may be updated to be more flexible in the future. See Possible Future Updates section at end of this readme.

## Setup and Run
Note: I used the below instructions on a Ubuntu terminal on Windows.

Clone repo and change into directory:
> git clone https://github.com/danwan754/job-scraper.git<br>
> cd job-scraper<br>

Create a virtual environment and activate it:
> python3 -m venv ./venv<br>
> source ./venv/bin/activate<br>


Install dependencies:
> pip3 install scrapy<br>

Set email credentials in config.json:
> {<br>
>     "sender_email": "\<sender gmail address\>",<br>
>     "sender_password": "\<sender password\>",<br>
>     "receiver_email": "\<receiver gmail address\>"<br>
> }

Run:
> scrapy crawl indeed -o indeed.json<br>
> python3 run.py<br>

You should receive an email with a list of developer jobs.

Repeating runs will require a pre-step to remove the indeed.json output file:
> rm indeed.json<br>
> scrapy crawl indeed -o indeed.json<br>
> python3 run.py<br>


## Setup task to run periodically on Windows Task Scheduler
Setup to automatically and periodically scrape and receive emails on new job postings on Windows Task Scheduler.
The *scrape_indeed.sh* script was written to be used as an argument in the new task creation.

In *scrape_indeed.sh*, replace the *\<full project path\>* with the absolute path to the */job-scraper* directory. (Ex. */mnt/c/Users/Dan/Projects/job-scraper*)

1) Open the Windows Task Scheduler.
2) Click the Create Task action.
3) In the General tab, give the task a name and description. Then click OK.
4) In the Triggers tab, create a new trigger that will initiate the task (ex. Daily, 10 pm). Then click OK.
5) In the Action tab, create a new action. The program/script field will be *C:\Windows\System32\WindowsPowerShell\v1.0* and the argument field will be *"bash.exe -c 'source \<full project path\>/scrape_indeed.sh'"* (copy this exactly, including the " and ' quote characters, and replace \<full project path\> with the same path you provided in *scrape_indeed.sh*). Then click OK.
6) Click OK, and you may be prompted to enter your computer login credential which you will provide. Done.

If there are new job postings, you should receive email during the trigger schedule that you selected.


## Possible Future Updates
1) Take inputs: job search keywords, location keywords (currently it only search for developer jobs in Vancouver, BC)
2) Crontab: easy crontab setup (currently made and tested for Task Scheduler on Windows)
3) Powershell only: clean up setup process to use powershell only (currently using powershell to run bash shell and script)
4) Use database: clean up directory structure by using a SQLite database (currently storing data in CSV and JSON files)
