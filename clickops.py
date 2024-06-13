import re
import json
import logging
from config import config


def identify_operation(json_file):

    """
    Identifies the operation type (Read or Write) and Clickops usage based on a JSON file.

    Args:
        json_file (str): Path to the JSON file containing the event data.

    Returns:
        "False": Indicates ClickOps usage based on the user agent.
        "True" (Read Operation): Signifies a read operation identified through the event name.
        "True" (Write Operation): Implies a write operation if neither ClickOps usage nor a read operation pattern match is found.
    """

    logging.basicConfig(filename='error.log', level=logging.ERROR)  # Configuring logging to a file

    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
       
            user_agent = data.get('userAgent')
            if user_agent is None:
                raise ValueError("No user agent found in JSON data.")
                
            
            event_name = data.get('eventName')

            if re.search(config["read_operation_pattern"], event_name):
                return "True" #Read Operation
            elif user_agent in config["clickops_user_agents"] or any (user_agent.startswith(prefix) for prefix in (tuple(config["clickops_prefixes"]))):
                return "False"
            else:
                return "True" #Write Operation
               
    except ValueError as e:
        logging.error(e)
    except FileNotFoundError:
        logging.error("No user agent found in JSON data.")
    except json.JSONDecodeError as e:
        logging.error ("Error decoding JSON")
    
