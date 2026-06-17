from difflib import HtmlDiff


def generate_html_diff(text1, text2):

    diff = HtmlDiff(wrapcolumn=120)

    html = diff.make_file(
        text1.splitlines(),
        text2.splitlines(),
        "Legacy Policy",
        "Modernized Policy"
    )

    return html
