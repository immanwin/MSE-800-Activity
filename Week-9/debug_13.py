import logging

logging.basicConfig(
    filename="student.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

student = "Ali"
marks = [10, 7, 3]

logging.info("Arambam!")
logging.info("Student: %s", student)

average = sum(marks) / len(marks)
logging.info("Average calculated: %.2f", average)

if average < 50:
    logging.warning("Student average is below 50")

logging.info("Mudivu!")
