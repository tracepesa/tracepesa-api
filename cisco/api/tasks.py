from cisco.api.service import parse_config_from_dir, links_update_or_create
import time
from background_task import background


@background(schedule=1)
def parse_config_background(dir):
    start = time.time()
    print('Parsing configs on dir: ' + dir)
    parse_config_from_dir(dir)
    print('Creating links:')
    links_update_or_create()
    end = time.time() - start
    print('Execution finished:' + str(round(end, 2)) + ' sec')
