
def calculate_grade(points):
    """Calculates the letter grade based on the points."""
    if 900 <= points <= 1000:
        return 'A'
    elif 800 <= points < 900:
        return 'B'
    elif 700 <= points < 800:
        return 'C'
    elif 600 <= points < 700:
        return 'D'
    elif 0 <= points < 600:
        return 'F'
    else:
        return 'Invalid Points'

def process_record(line, read_count, outfile_grades, outfile_error):
    """Processes a single line of data and writes to the appropriate file."""
    data = line.strip().split(',')
    if len(data) == 3:
        try:
            student_id = data[0].strip()
            name = data[1].strip()
            points_str = data[2].strip()
            points = int(points_str)

            if 0 <= points <= 1000:
                grade = calculate_grade(points)
                grade_record = f"{student_id},{read_count},{name},{points},{grade}\n"
                outfile_grades.write(grade_record)
                return 1, 0
            elif points < 0:
                error_record = f"{student_id},{read_count},{name},{points},Points cannot be negative\n"
                outfile_error.write(error_record)
                return 0, 1
            elif points > 1000:
                error_record = f"{student_id},{read_count},{name},{points},Points cannot be greater than 1000\n"
                outfile_error.write(error_record)
                return 0, 1
            elif points == 1000:
                grade_record = f"{student_id},{read_count},{name},{points},Base Point\n"
                outfile_grades.write(grade_record)
                return 1, 0
        except ValueError:
            error_record = f"{data[0].strip()},{read_count},{data[1].strip()},{points_str},Points must be numeric\n"
            outfile_error.write(error_record)
            return 0, 1
    else:
        error_record = f"Invalid data format: {line.strip()}\n"
        outfile_error.write(error_record)
        return 0, 1

def process_data(input_file, grades_file, error_file):
    """Reads data from the input file, processes it, and writes to grade or error files."""
    read_count = 0
    good_count = 0
    error_count = 0

    try:
        with open(input_file, 'r') as infile, \
             open(grades_file, 'w') as outfile_grades, \
             open(error_file, 'w') as outfile_error:

            line = infile.readline()
            while line != "":
                read_count += 1
                good, error = process_record(line, read_count, outfile_grades, outfile_error)
                good_count += good
                error_count += error
                line = infile.readline()

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        return 0, 0, 0

    return read_count, good_count, error_count

def main():
    """Main function to run the grade processing program."""

    input_filename = 'points.txt'
    grades_filename = 'grades.txt'
    error_filename = 'error.txt'

    records_read, good_records, error_records = process_data(input_filename, grades_filename, error_filename)

    print("\nProcessing Complete:")
    print(f"Total records read: {records_read}")
    print(f"Good records written to {grades_filename}: {good_records}")
    print(f"Error records written to {error_filename}: {error_records}")

    

if __name__ == "__main__":
    main()
