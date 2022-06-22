# Mark it done job

This python project is designed to work as a Cron job.  It scans your todoist projects for boards, for each board it finds it looks for your choosen "Done" column and any todo's which aren't marked as complete it completes them for you.

# Getting started

```
pip install -r requirements.txt
cp exmmple_config.yml config.yml
```

Update the config yaml with your API key from todoist.  Then you can just run the script using:

```
./mark-it-done.py
```

# Alternatively...

I've set the script up now as a GitHub action so in theory you can fork the repo add your API key to GitHub Screets and have it run on your terms.
