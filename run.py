""" This is the main file that serves as the entry point of the program. """
import logging
import logging.config
import yaml


def main():
    """
    This is the main function that serves as the entry point of the program.
    """
    config = yaml.safe_load(open('configs/xetra_report1_config.yml'))
    #print(config)

    log_config = config['logging']
    logging.config.dictConfig(log_config)   # load the config as a dictionary
    logger = logging.getLogger(__name__)    # create logger using the name of the file
    logger.info('Starting the program')

if __name__ == "__main__":
    main()