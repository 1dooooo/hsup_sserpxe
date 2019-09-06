import logging as log

logger = log.basicConfig(level=log.WARNING, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                         datefmt='%a, %d %b %Y %H:%M:%S', handlers={log.FileHandler(filename='test.log', mode='a', encoding='utf-8')})
