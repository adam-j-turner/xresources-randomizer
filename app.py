from flask import Flask, Response
from jinja2 import Environment, FileSystemLoader
import random

app = Flask('xresources-randomizer')

jinjaEnv = Environment(
  loader=FileSystemLoader('templates/')
)

template = jinjaEnv.get_template('xresources.j2')

@app.route('/')
def renderMain():
    return Response(
      template.render(colors=[randomHexColor() for i in range(0,22)]),
      mimetype='text/plain'
    )

def randomHexColor():
  return "%06x" % random.randint(0, 0xFFFFFF)
