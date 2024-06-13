import markdown


class MarkdownClassesExtension(markdown.Extension):

    # Ref: https://github.com/mikitex70/plantuml-markdown/blob/master/plantuml_markdown/plantuml_markdown.py#L670
    def extendMarkdown(self, md: markdown.Markdown):
        pass