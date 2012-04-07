from sphinx.builders.html import StandaloneHTMLBuilder, SingleFileHTMLBuilder
from docutils.writers.html4css1 import HTMLTranslator as BaseTranslator, Writer as BaseWriter
from sphinx.directives import TocTree

class HTML5Translator(BaseTranslator):
	def __init__(self, builder, *args, **kwds):
		BaseTranslator.__init__(self, *args, **kwds)
		self.builder = builder

	def visit_section(self, node):
		self.section_level += 1
		self.body.append(
			self.starttag(node, 'section'))
	def depart_section(self, node):
		self.section_level -= 1
		self.body.append('</section>\n')

	def visit_literal_block(self, node):
		self.body.append('<pre class="literal-block"><code>\n')
	def depart_literal_block(self, node):
		self.body.append('\n</code></pre>\n')

	def visit_list_item(self, node):
		self.body.append(self.starttag(node, 'li', CLASS='fragment'))
		if len(node):
			node[0]['classes'].append('first')

	def depart_list_item(self, node):
		self.body.append('</li>\n')

	def unknown_visit(self, node):
		self.document.reporter.warning('Ignoring node: %s' % node.tagname)
	def unknown_departure(self, node): pass

	# Ignore conditional "only" nodes
	def visit_only(self, node): pass
	def depart_only(self, node): pass

class HTML5Writer(BaseWriter):
	def __init__(self):
		BaseWriter.__init__(self)
		self.translator_class = HTML5Translator

class StandaloneHTML5Builder (StandaloneHTMLBuilder):
	name = 'html5'

	def init_translator_class(self):
		self.translator_class = HTML5Translator

class SingleFileHTML5Builder (SingleFileHTMLBuilder):

	name = 'singlehtml5'

	def init_translator_class(self):
		self.translator_class = HTML5Translator


def setup (sphinx):
	sphinx.add_builder(StandaloneHTML5Builder)
	sphinx.add_builder(SingleFileHTML5Builder)
