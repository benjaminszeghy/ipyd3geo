project = "ipyd3geo"
author = "Benjamin Szeghy"
copyright = "2026, Benjamin Szeghy"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "myst_parser",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

exclude_patterns = ["superpowers"]

html_theme = "pydata_sphinx_theme"

autodoc_member_order = "bysource"
