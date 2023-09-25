from lxml import etree, html

IGNORE="ignore"
IGNORE_START="<%s>" % IGNORE
IGNORE_END="</%s>" % IGNORE

def _parse(s):
    return html.fragment_fromstring(
        "%s%s%s" % (IGNORE_START, s, IGNORE_END))

def _serialize(tree):
    return etree.tostring(
        tree, method='html', encoding="unicode").removeprefix(
            IGNORE_START).removesuffix(IGNORE_END)

def verbosify(s):
    parsed = _parse(s)

    try:
        verbosified = _verbosify_node(parsed)
    except Exception as e:
        raise Exception("Parsing %r" % s) from e

    return _serialize(verbosified)

def _verbosify_text(text, skip_mrow=False):
    substrings = text.split()
    if len(substrings) == 0:
        return []
    for substring in substrings:
        row = []
        partial_number = []

        def maybe_save_number():
            if partial_number:
                element = etree.Element("mn")
                element.text = "".join(partial_number)
                partial_number.clear()
                row.append(element)

        for char in substring:
            if char.isdigit():
                partial_number.append(char)
            elif char.isalpha():
                maybe_save_number()
                element = etree.Element("mi")
                element.text = char
                row.append(element)
            else:
                maybe_save_number()
                element = etree.Element("mo")
                element.text = char
                row.append(element)
        maybe_save_number()

        if len(row) == 1:
            element, = row
        elif skip_mrow:
            yield from row
        else:
            element = etree.Element("mrow")
            element.extend(row)
        yield element

def _verbosify_node(node):
    skip_mrow = node.tag in ["mrow", "mtd", IGNORE]
    
    new_node = etree.Element(node.tag)
    if node.text:
        if node.tag in ["mi", "mn", "mo"]:
            new_node.text = node.text
        else:
            new_node.extend(_verbosify_text(node.text, skip_mrow))

    for child in node:
        new_node.append(_verbosify_node(child))
        if child.tail:
            new_node.extend(_verbosify_text(child.tail, skip_mrow))

    return new_node
