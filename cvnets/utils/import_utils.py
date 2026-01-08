#
# For licensing see accompanying LICENSE file.
# Copyright (C) 2023 Apple Inc. All Rights Reserved.
#

import importlib
import os
from typing import Sequence

from cvnets.common import LIBRARY_ROOT
from cvnets.utils import logger


def import_modules_from_folder(
    folder_name: str, extra_roots: Sequence[str] = ()
) -> None:
    """Automatically import all modules from public library root folder, in addition
    to the @extra_roots directories.

    The @folder_name directory must exist in LIBRARY_ROOT, but existence in @extra_roots
    is optional.

    Args:
        folder_name: Name of the folder to search for its internal and public modules.
        extra_roots: By default, this function only imports from
            `LIBRARY_ROOT/{folder_name}/**/*.py`. For any extra_root provided, it will
            also import `LIBRARY_ROOT/{extra_root}/{folder_name}/**/*.py` modules.
    """
    if not LIBRARY_ROOT.joinpath(folder_name).exists():
        # lazy loading handling: skip if the main folder does not exist
        return
    
    # python 3.12+ compatibility: use rglob instead of glob with recursive
    search_roots = [LIBRARY_ROOT / folder_name]
    for extra in extra_roots:
        search_roots.append(LIBRARY_ROOT / extra / folder_name)
        
    for root in search_roots:
        if not root.exists():
            continue
        for path in root.rglob("*.py"):
            filename = path.name
            if filename[0] not in (".", "_"):
                module_name = (
                    path.relative_to(LIBRARY_ROOT)
                    .with_suffix("")
                    .as_posix()
                    .replace("/", ".")
                )
                importlib.import_module(module_name)
