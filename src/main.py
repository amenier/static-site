import logging
import shutil
import os
import sys
from logging_config import setup_logging
setup_logging()
from copy_static import copy_static_to_docs
from generate_page import generate_page, generate_pages_recursive

def main():
    logger = logging.getLogger(__name__)
    logger.debug("main function started")
    if len(sys.argv) < 2:
        basepath = "/"
    else:
        basepath = sys.argv[1]
    if os.path.exists("./docs"):
        logger.debug("removing docs")
        shutil.rmtree("./docs")
    else:
        logger.debug("no docs directory to remove")
    os.mkdir("./docs")
    copy_static_to_docs("./static", "./docs")
    logger.debug("files copied")
    #generate_page("./content/index.md","template.html","./docs/index.html")
    generate_pages_recursive("./content", "./template.html", "./docs", basepath)

if __name__ == "__main__":
    main()