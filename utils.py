import json


def load_json() -> list[dict]:
    with open('candidates.json', 'r', encoding='utf-8') as file:
        candidates = json.load(file)
        return candidates


def get_all_candidates():
    return load_json()


def get_candidate_by_pk(pk):
    for candidate in load_json():
        if candidate['id'] == pk:
            return candidate
    return 'Not Found'


def get_candidate_by_name(username):
    result = []
    for candidate in load_json():
        if username.lower() in candidate['name'].lower():
            result.append(candidate)
    return result


def get_candidate_by_skill(skill):
    result = []
    for candidate in load_json():
        skills = candidate['skills'].lower().split(', ')
        if skill in skills:
            result.append(candidate)
    return result
