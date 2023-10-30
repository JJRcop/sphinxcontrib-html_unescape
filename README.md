# Sphinxcontrib-html_unescape
Call html.unescape on source files when building docs

This converts named HTML character references: like '`&gt;`' into '`<`',
and numeric references: like '`&#128270;`' into '`🔎`'

See https://docs.python.org/3/library/html.html#html.unescape
and https://html.spec.whatwg.org/multipage/named-characters.html#named-character-references
for more information on available sequences
