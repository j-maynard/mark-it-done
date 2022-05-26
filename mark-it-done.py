#!/usr/bin/env python3
import yaml
from todoist_api_python.api import TodoistAPI

def process_tasks(api, s_id, s_name, p_name):
    tasks = api.get_tasks(section_id = s_id)
    if len(tasks) == 0:
        return
    print(f"Completing tasks in the {s_name} section of {p_name}")
    for t in tasks:
        print(f"\tMarking task \"{t.content}\" as complete")
        api.close_task(task_id=t.id)

def process_sections(api, p):
    sections = api.get_sections(project_id=p.id)
    if len(sections) == 0:
        return
    done_sections_names = list(set.intersection(*map(set, [config['done_columns'], 
        list(map(lambda s: s.name, sections))]))) 
    done_sections = list(filter(lambda s: s.name in done_sections_names, sections))
    for s in done_sections:
        process_tasks(api, s.id, s.name, p.name)

with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

api = TodoistAPI(config['api_key'])

try:
    projects = api.get_projects()
    for p in projects:
        process_sections(api, p)
except Exception as error:
    print(error)
