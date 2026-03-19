#!/usr/bin/env python3

# Script to generate HTML articles with correct numbering

sections = {
    "Works": "Work",
    "Latest news": "Article",
    "Testimonials": "Testimonial"
}

html_output = ""

for section_name, item_name in sections.items():
    html_output += f"<section id='{section_name.lower().replace(' ', '-')}'>\n"
    html_output += f"    <h2>{section_name}</h2>\n"
    for i in range(1, 4):
        html_output += f"    <article>{item_name} {i}</article>\n"
    html_output += "</section>\n\n"

print(html_output)
