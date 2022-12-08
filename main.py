from flask import Flask, render_template

import utils

app = Flask(__name__)


@app.route("/")
def index():
    candidates = utils.get_all_candidates()
    return render_template('list.html', candidates=candidates)


@app.route("/candidates/<int:pk>")
def get_candidate(pk):
    candidate = utils.get_candidate_by_pk(pk)
    return render_template('card.html', candidate=candidate)


@app.route("/search/<candidate_name>")
def get_candidates_by_name(candidate_name):
    candidates = utils.get_candidate_by_name(candidate_name)
    return render_template('search.html', candidates=candidates, count=len(candidates))


@app.route("/skill/<skill>")
def get_candidates_by_skills(skill):
    candidates = utils.get_candidate_by_skill(skill.lower())
    return render_template('skills.html', candidates=candidates, count=len(candidates), skill=skill)


# app.run()
app.run(host='0.0.0.0', port=4995)
