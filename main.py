"""
Main application runner
"""

from pathlib import Path
import sys
from pipeline.scamdetctor.detector import ScamDetector
from utils import get_logger

#path normalization
project_root = Path(__file__).parent
sys.path.append(str(project_root))
logger = get_logger(__name__)

# main runner function - calls scam detection workflow
def main():
        """
        Main function to run the scam detection workflow.
        """
        detector = ScamDetector()
        # test_message = "You have an unclaimed policy for $10000, fill the details to claim it, otherwise it will expire in the next 2 hours."
        test_message = input("Enter the message to check for scam: ")

        try:
            logger.info("Running the scam detection workflow...")
            result = detector.run(test_message)
            print(f"Detection Result: {result}")
            logger.info("Scam detection workflow completed successfully.")
        except Exception as e:
            logger.error(f"Error occured during scam detection: {e}")

if __name__ == "__main__":
    main()