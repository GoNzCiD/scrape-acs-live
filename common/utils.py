def trim_html(html_str):
    result = html_str.replace("\n", "")
    result = result.replace("\"", "'")
    return result