# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))


# -- Project information -----------------------------------------------------

project = 'Entregas da Equipe Rocket'
copyright = '2021, Equipe Rocket'
authors = 'André da Silva Barbosa, ' \
          'Frederick Moschkowich, ' \
          'Jackson Querubin, ' \
          'Jonios Maximo, ' \
          'Rodrigo Renie'
show_authors = True

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.extlinks',
    'sphinxcontrib.programoutput'
]

# Looks for objects in external projects
# intersphinx_mapping = {
#     'nltk': ('https://nltk.readthedocs.io/en/latest/', None),
# }

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'pt_BR'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
# html_theme = "aiohttp_theme"
# html_theme = 'bootstrap-limix'
# extensions.append("faculty_sphinx_theme")
# html_theme = "faculty-sphinx-theme"
html_theme_options = {
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 2,
    'includehidden': True,
    'titles_only': False
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Extension configuration -------------------------------------------------

extlinks = {
    'nltk': ('https://www.nltk.org', 'NLTK'),
    'github_rodrigorenie': ('https://github.com/rodrigorenie/%s', None),
    'github_entregas': ('https://github.com/rodrigorenie/entregas/%s', None),
    'ta-aula': ('https://docs.google.com/document/d/13s6jq6--Ouh3eGQ8qKt1urZbT49Sq2eXM2drTfZT0EQ/%s', None),
    'ta-p0': ('https://docs.google.com/document/d/1eZew1Qwm64EyAbaiL5Xt8owmttOH9YGo/%s', None),
    'ta-p1': ('https://docs.google.com/document/d/1DMUES7vDRG0ubwjYIjR5KbUh2MLIeE9r/%s', None),
    'ta-p2': ('https://docs.google.com/document/d/15Bsq4fk7fs2MRFMHjVLL0R5fvptTJovz/%s', None),
    'ta-final': ('https://docs.google.com/document/d/13SZAiID1Qth1ywr5RxHFT5TGnzksLFvi/%s', None),
    'ml-at': ('https://docs.google.com/document/d/1BTSezlm_hMFStU6UHfdUO2DHyjF5Vf64/%s', None),
    'ml-final': ('https://docs.google.com/document/d/1BTSezlm_hMFStU6UHfdUO2DHyjF5Vf64/%s', None)
}

# https://github.com/readthedocs/sphinx_rtd_theme/issues/117#issuecomment-41506687
#
def setup(app):
    app.add_css_file("theme_overrides.css")
