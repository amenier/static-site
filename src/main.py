import logging
import shutil
import os
from logging_config import setup_logging
setup_logging()
from copy_static import copy_static_to_public
from generate_page import generate_page, generate_pages_recursive

def main():
    logger = logging.getLogger(__name__)
    logger.debug("main function started")
    if os.path.exists("./public"):
        logger.debug("removing public")
        shutil.rmtree("./public")
    else:
        logger.debug("no public directory to remove")
    os.mkdir("./public")
    copy_static_to_public("./static", "./public")
    logger.debug("files copied")
    #generate_page("./content/index.md","template.html","./public/index.html")
    generate_pages_recursive("./content", "./template.html", "./public")

if __name__ == "__main__":
    main()