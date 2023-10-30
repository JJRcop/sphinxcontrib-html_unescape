# Copyright 2023 Jonathan Rubenstein
#
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


# Call html.unescape on source files when building docs
#
# This converts named HTML character references: like '&gt;' into '>',
# and numeric references: like '&#128270;' into '🔎'
#
# See https://docs.python.org/3/library/html.html#html.unescape
# and https://html.spec.whatwg.org/multipage/named-characters.html#named-character-references
# for more information on available sequences

from html import unescape

# For type hints (PEP 484)
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment


def unescape_source(app: Sphinx, docname: str, source: list) -> None:
    env: BuildEnvironment = app.env
    exclude: list = env.config.html_unescape_exclude
    onlyinclude: list = env.config.html_unescape_onlyinclude
    docpath: str = env.doc2path(docname, base=False)
    if docname in exclude:
        return
    if docpath in exclude:
        return
    if len(onlyinclude) and not (docname in onlyinclude or docpath in onlyinclude):
        return
    source[0] = unescape(source[0])


def setup(app: Sphinx) -> dict[str, bool | str]:
    app.add_config_value('html_unescape_exclude', [], 'env', [list])
    app.add_config_value('html_unescape_onlyinclude', [], 'env', [list])
    app.connect('source-read', unescape_source)
    return {
        'version': '1.0',
        'env_version': '1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
