from pathlib import Path


LESSON_TEMPLATE = """# Description
print("--------------------------------------------------")




# Assignment
print("-------------------------Assignment-------------------------")

print("-------------------------End of Assignment-------------------------")
"""


def create_lessons(
    output_directory: Path, first_lesson: int, last_lesson: int
) -> None:
    if first_lesson < 1 or last_lesson < first_lesson:
        raise ValueError("Enter a positive range with the first lesson at or before the last.")

    output_directory.mkdir(parents=True, exist_ok=True)
    for lesson_number in range(first_lesson, last_lesson + 1):
        lesson_path = output_directory / f"Lesson{lesson_number}.py"
        try:
            with lesson_path.open("x", encoding="utf-8") as lesson_file:
                lesson_file.write(LESSON_TEMPLATE)
        except FileExistsError:
            print(f"Skipped {lesson_path.name} (already exists)")
        else:
            print(f"Created {lesson_path.name}")


if __name__ == "__main__":
    output_directory_input = input("Output directory: ").strip()
    try:
        if not output_directory_input:
            raise ValueError("Output directory cannot be empty.")
        output_directory = Path(output_directory_input).expanduser()
        first_lesson = int(input("First lesson number: "))
        last_lesson = int(input("Last lesson number (inclusive): "))
        create_lessons(output_directory, first_lesson, last_lesson)
    except ValueError as error:
        print(f"Invalid input: {error}")
