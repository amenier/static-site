from markdown_to_html import markdown_to_html_node
import os
import logging

logger = logging.getLogger(__name__)

def extract_title(markdown):
    with open(markdown, "r") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("# "):
                return line[2:].strip()
        raise ValueError("missing title")
    
def generate_page(from_path, template_path, dest_path):
    logger.info(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path,"r") as f:
        md = f.read()
        f.close()
    
    with open(template_path, "r") as g:
        template = g.read()
        logger.debug(template)
        g.close()
    
    html_nodes = markdown_to_html_node(md)

    html = html_nodes.to_html()

    title = extract_title(from_path)

    logger.info("Replacing content")
    template = template.replace("{{ Title }}", title).replace("{{ Content }}", html)
    logger.debug(template)

    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))
    
    with open(dest_path,"w") as h:
        # template_lines = template.split("\n")
        # for line in template_lines:
        #     h.write(line)
        h.write(template)
        h.close()
    
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    logger.debug("starting recursive page generation")
    # source_dir = os.path.dirname(dir_path_content)
    # dest_dir = os.path.dirname(dest_dir_path)
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
        logger.debug(f"created {dest_dir_path}")
    items = os.listdir(dir_path_content)
    for item in items:
        logger.debug(f"attempting to copy {item}")
        if os.path.isfile(os.path.join(dir_path_content, item)):
            logger.debug(f" current item is {os.path.join(dir_path_content, item)}")
            generate_page(os.path.join(dir_path_content, item), template_path, os.path.join(dest_dir_path, item).replace(".md",".html"))
        else:
            generate_pages_recursive(os.path.join(dir_path_content, item), template_path, os.path.join(dest_dir_path, item))
