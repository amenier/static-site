import os
import shutil
import logging


def copy_static_to_public(src, dest):
    logger = logging.getLogger(__name__)
    logger.debug("checking for destination")
    if not os.path.exists(dest):
        os.mkdir(dest)
        logger.debug(f"created {dest}")
    items = os.listdir(src)
    for item in items:
        logger.debug(f"attempting to copy {item}")
        if os.path.isfile(os.path.join(src, item)):
            logger.debug(f" current item is {os.path.join(src, item)}")
            shutil.copy(os.path.join(src, item), os.path.join(dest, item))
        else:
            os.mkdir(os.path.join(dest, item))
            copy_static_to_public(os.path.join(src, item), os.path.join(dest, item))



    