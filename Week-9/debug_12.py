import logging

logging.basicConfig(level=logging.WARNING)

name = "Farah"
marks = [65, 72, 80]

logging.debug("Marks list created")
logging.info("Processing student: %s", name)
logging.info("Number of marks: %d", len(marks))
logging.warning("This is a test warning")
logging.error("This is a test error")
