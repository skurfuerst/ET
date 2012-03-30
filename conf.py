import sys, os

sys.path.append(os.path.abspath('builders'))

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
	'sphinx.ext.autodoc',
	'sphinx.ext.intersphinx',
	'sphinx.ext.todo',
	'sphinx.ext.ifconfig',
	'sphinx.ext.viewcode',
	'html5'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'TYPO3'
copyright = u''

# The short X.Y version.
version = ''
# The full version, including alpha/beta/rc tags.
release = ''

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Configure PHP syntax highlighting
# all textsnippets will be PHP by default
highlight_language = 'html'

# ... and we do not want to include <?php ... ?> in the PHP code snippets.
from sphinx.highlighting import lexers
from pygments.lexers.web import PhpLexer
lexers['php'] = PhpLexer(startinline=True)

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'revealjs'
html_show_copyright = False

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = [ 'themes' ]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = project + " " + release

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = ''


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Output file base name for HTML help builder.
htmlhelp_basename = 'EmberJSTutorial'

html_use_index = False

# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('Index', 'emberjstutorial', u'TYPO3',
     [u'TYPO3'], 1)
]


# -- Options for Epub output ---------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'TYPO3'
epub_author = u'TYPO3'
epub_publisher = u'TYPO3'
epub_copyright = u''

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'http://docs.python.org/': None}

rst_prolog = """
.. |documentationNotReady| replace:: Dit deel van het handboek is nog niet af.

"""
