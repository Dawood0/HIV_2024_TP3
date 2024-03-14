import random

def generate_html(num_tags=5, max_depth=3):
    opening_tags = ["<html>", "<head>", "<title>", "<meta>", "<body>", "<h1>", "<p>", "<div>", "<span>", "<img>", "<a>", "<ul>", "<li>"]
    closing_tags = ["</html>", "</head>", "</title>", "</meta>", "</body>", "</h1>", "</p>", "</div>", "</span>", "</img>", "</a>", "</ul>", "</li>"]
    html = ""
    stack = []
    for _ in range(num_tags):
        tag_index = random.randint(0, len(opening_tags) - 1)
        tag = opening_tags[tag_index]
        html += tag
        if tag in ["<html>", "<head>", "<body>", "<div>", "<span>", "<ul>"]:
            stack.append(closing_tags[tag_index])
    while stack:
        closing_tag = stack.pop()
        html += closing_tag
    return html

if __name__ == "__main__":
    html_code = generate_html()
    print(html_code)
