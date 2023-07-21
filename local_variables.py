from dotenv import load_dotenv
import os


# Load local variables
load_dotenv()


class Links:
    
    def __init__(self):
        self.survey = os.getenv("SURVEY")
        self.projects = os.getenv("PROJECTS")
        self.approved = os.getenv("APPROVED")
        self.start_points = os.getenv("START_POINTS")
        self.end_points = os.getenv("END_POINTS")

        