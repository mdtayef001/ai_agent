import os

# from utils.config import MAX_CHARS


def get_file_content(working_directory, file_path):
    try:
        working_dir_ads = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(working_dir_ads, file_path))
        MAX_CHARS = 10000

        if (
            not os.path.commonpath([working_dir_ads, target_file_path])
            == working_dir_ads
        ):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(target_file_path, "r") as f:
            file_content = f.read(MAX_CHARS)
            if f.read(1):
                file_content += (
                    f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )
            return file_content

    except Exception as e:
        return f"Error: {str(e)}"


# result = get_file_content("/home/tayef/code/Boot.dev/ai_agent/calculator", "lorem.txt")
# print(result)
