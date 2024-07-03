# import os
# import html2text

# def html_to_markdown(html_content):
#     # Create an instance of HTML2Text and configure options
#     h = html2text.HTML2Text()
#     h.ignore_links = True  # Set to True to ignore links
#     h.ignore_images = True  # Set to True to ignore images
#     h.bypass_tables = False  # Set to True to bypass tables

#     # Convert HTML to Markdown
#     return h.handle(html_content)

# def convert_html_files_in_directory(input_directory, output_directory):
#     # Walk through all files and directories within the input directory
#     for root, dirs, files in os.walk(input_directory):
#         for file in files:
#             if file.endswith('.html'):
#                 # Construct the full file path
#                 html_file_path = os.path.join(root, file)

#                 # Read the HTML content from the file
#                 with open(html_file_path, 'r', encoding='utf-8') as html_file:
#                     html_content = html_file.read()

#                 # Convert HTML to Markdown
#                 markdown_content = html_to_markdown(html_content)

#                 # Create the corresponding Markdown file path
#                 relative_path = os.path.relpath(html_file_path, input_directory)
#                 markdown_file_path = os.path.join(output_directory, os.path.splitext(relative_path)[0] + '.md')

#                 # Ensure the output directory exists
#                 os.makedirs(os.path.dirname(markdown_file_path), exist_ok=True)

#                 # Write the Markdown content to the file
#                 with open(markdown_file_path, 'w', encoding='utf-8') as markdown_file:
#                     markdown_file.write(markdown_content)

#                 print(f'Converted: {html_file_path} -> {markdown_file_path}')

# # Example usage
# input_directory = 'C:/Users/matth/test_doc_site/my-website/articles_organized'  # Replace with your input directory
# output_directory = 'C:/Users/matth/test_doc_site/my-website/md_organized'  # Replace with your output directory
# convert_html_files_in_directory(input_directory, output_directory)


import os
import html2text
from bs4 import BeautifulSoup

def html_to_markdown(html_content):
    # Create an instance of HTML2Text and configure options
    h = html2text.HTML2Text()
    h.ignore_links = True  # Set to True to ignore links
    h.ignore_images = True  # Set to True to ignore images
    h.bypass_tables = False  # Set to True to bypass tables

    # Convert HTML to Markdown
    return h.handle(html_content)

def extract_first_heading(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    first_heading = soup.find(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    if first_heading:
        return first_heading.get_text().strip()
    return None

def add_slug_to_markdown(markdown_content, slug):
    slug_line = f'---\nslug: {slug.lower().replace(" ", "-")}\n---\n\n'
    return slug_line + markdown_content

def convert_html_files_in_directory(input_directory, output_directory):
    # Walk through all files and directories within the input directory
    for root, dirs, files in os.walk(input_directory):
        for file in files:
            if file.endswith('.html'):
                # Construct the full file path
                html_file_path = os.path.join(root, file)

                # Read the HTML content from the file
                with open(html_file_path, 'r', encoding='utf-8') as html_file:
                    html_content = html_file.read()

                # Extract the first heading to create the slug
                heading = extract_first_heading(html_content)
                if heading:
                    slug = heading
                else:
                    slug = 'default-slug'

                # Convert HTML to Markdown
                markdown_content = html_to_markdown(html_content)

                # Add the slug to the Markdown content
                markdown_content_with_slug = add_slug_to_markdown(markdown_content, slug)

                # Create the corresponding Markdown file path
                relative_path = os.path.relpath(html_file_path, input_directory)
                markdown_file_path = os.path.join(output_directory, os.path.splitext(relative_path)[0] + '.md')

                # Ensure the output directory exists
                os.makedirs(os.path.dirname(markdown_file_path), exist_ok=True)

                # Write the Markdown content to the file
                with open(markdown_file_path, 'w', encoding='utf-8') as markdown_file:
                    markdown_file.write(markdown_content_with_slug)

                print(f'Converted: {html_file_path} -> {markdown_file_path}')

# Example usage
input_directory = 'C:/Users/matth/test_doc_site/my-website/articles_organized'  # Replace with your input directory
output_directory = 'C:/Users/matth/test_doc_site/my-website/md_organized_converted'  # Replace with your output directory
convert_html_files_in_directory(input_directory, output_directory)
