# SPDX-License-Identifier: MIT OR Apache-2.0
# SPDX-FileCopyrightText: The Coding Guidelines Subcommittee Contributors

from docutils import nodes
from sphinx.roles import SphinxRole
from urllib.parse import quote

class StdRefRole(SphinxRole):
    def run(self):
        text, target = parse_target_from_text(self.text)
        url = f"{self.env.config.spec_std_docs_url}/?search={quote(target)}"

        node = nodes.reference(internal=False, refuri=url)
        node += nodes.literal("", text)

        return [node], []


def parse_target_from_text(text):
    if "<" in text and text.endswith(">"):
        target_start = text.rfind("<")
        target = text[target_start + 1 : len(text) - 1]
        text = text[:target_start].rstrip()
    elif "[" in text and "]" in text:
        target = text[text.find("[") + 1 : text.rfind("]")]
        text = text.replace("[", "").replace("]", "")
    else:
        target = text

    return text, target
