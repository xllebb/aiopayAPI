# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


project = 'aiopayAPI'
copyright = '2023, xllebb'
author = 'xllebb'
release = '0.1.3.8'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'ru'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
autodoc_member_order = 'bysource'
html_static_path = ['_static']

from pygments.lexer import RegexLexer
from pygments import token
from sphinx.highlighting import lexers

class BCLLexer(RegexLexer):
    name = 'MYLANG'

    tokens = {
        'root': [
            (r'MyKeyword', token.Keyword),
            (r'[a-zA-Z]', token.Name),
            (r'\s', token.Text)
        ]
    }

lexers['MYLANG'] = BCLLexer(startinline=True)