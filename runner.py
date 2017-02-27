#!/usr/bin/env python

import os
import json
from jinja2 import Environment, FileSystemLoader


PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)


def render_template(template_filename, posts, authors):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(posts = posts, authors=authors)


def create_index_html():
    fname = "output.html"
    postslist = open('posts.json', 'r')
    posts = json.load(postslist)
    authorslist = open('authors.json', 'r')
    authors = json.load(authorslist)

    with open(fname, 'w') as f:
        html = render_template('index.html',posts,authors).encode('utf-8').strip()
        f.write(html)


def main():
    create_index_html()

#############################################################################

if __name__ == "__main__":
    main()