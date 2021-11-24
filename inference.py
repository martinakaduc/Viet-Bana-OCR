import os
import shutil

bahnar_script = [
    "cd BanaOCR && python run.py",
    "cd BanaOCR && python correction.py"
]

vietnamese_script = [
    "cd VietOCR && python split_column.py",
    "cd VietOCR && python split_entry.py",
    "cd VietOCR && python ocr.py",
    "cd VietOCR && python txttodocx.py"
]

script_by_lang = {
    "Bahnaric": bahnar_script,
    "Vietnamese": vietnamese_script
}

def remove_files(folder, ext=None):
    for rm_file in os.listdir(folder):
        if rm_file.endswith(ext):
            os.remove(os.path.join(folder, rm_file))

def get_result(language, list_images):
    try:
        list_result_files = []

        if language == "Bahnaric":
            # Copy data
            for image in list_images:
                shutil.copy(os.path.join("upload_files", image), os.path.join("BanaOCR/input", image))
            
            # Run OCR
            for command in script_by_lang[language]:
                os.system(command)

            # Remove stuffs
            remove_files("upload_files", "png")
            remove_files("BanaOCR/input", "png")
            remove_files("BanaOCR/output", "txt")

            # Move result files
            list_result_files = list(filter(lambda x: x.endswith("txt"), os.listdir("BanaOCR/result")))
            for result_file in list_result_files:
                shutil.move(os.path.join("BanaOCR/result", result_file), os.path.join("result_files", result_file))

            if len(list_images) != len(list_result_files):
                return False, []

        elif language == "Vietnamese":
            # Copy data
            for image in list_images:
                shutil.copy(os.path.join("upload_files", image), os.path.join("VietOCR/images/001", image))

            # Run OCR
            for command in script_by_lang[language]:
                os.system(command)

            # Remove stuffs
            remove_files("upload_files", "png")
            remove_files("VietOCR/images/001", "png")
            remove_files("VietOCR/splitColumn/001", "png")
            remove_files("VietOCR/splitLine/001", "jpg")
            remove_files("VietOCR/texts/Tu dien Hoang Phe/results", "txt")

            # Move result files
            list_result_files = ["result.docx"]
            if not os.path.exists(os.path.join("VietOCR", list_result_files[0])):
                return False, []

            for result_file in list_result_files:
                shutil.move(os.path.join("VietOCR", result_file), os.path.join("result_files", result_file))

        return True, list_result_files

    except:
        return False, []