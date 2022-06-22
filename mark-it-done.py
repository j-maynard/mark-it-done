#!/usr/bin/env python3
import sys
from todoist_api_python.api import TodoistAPI
from pyaml_env import parse_config


def process_tasks(s_id, s_name, p_name):
    tasks = api.get_tasks(section_id = s_id)
    if len(tasks) == 0:
        return
    print(f"Completing tasks in the {s_name} section of {p_name}")
    for t in tasks:
        print(f"\tMarking task \"{t.content}\" as complete")
        api.close_task(task_id=t.id)

def process_sections(p):
    sections = api.get_sections(project_id=p.id)
    if len(sections) == 0:
        return
    done_sections_names = list(set.intersection(*map(set, [config['done_columns'], 
        list(map(lambda s: s.name, sections))]))) 
    done_sections = list(filter(lambda s: s.name in done_sections_names, sections))
    for s in done_sections:
        process_tasks(s.id, s.name, p.name)

config = {}
try:
    # Load Config
    with open('./config.yml', 'r') as file:
        config = parse_config('./config.yaml')
except Exception as error:
    print("Unable to load config file... Exiting.")
    sys.exit(1)

if "api_key" not in config:
    print("Unable to load API key from config... Exiting.")
    sys.exit(1)

# Create API object
api = TodoistAPI(config['api_key'])

try:
    projects = api.get_projects()
    for p in projects:
        process_sections(p)
except Exception as error:
    print(error)
