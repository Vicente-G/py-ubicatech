# Standard Library imports

# Core Flask imports

# Third-party imports
import bleach

# App imports


def strip_xss(text):
    """Remove all markup from text."""

    if not text:
        return None

    allowed_tags = []
    allowed_attributes = []
    allowed_styles = []

    return bleach.clean(
        text,
        allowed_tags,
        allowed_attributes,
        allowed_styles,
        strip=True,
        strip_comments=True,
    ).strip()
