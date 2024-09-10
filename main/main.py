import os
import shutil

def create_folder_with_docs():
    if getattr(sys, 'frozen', False):
        exe_dir = os.path.dirname(sys.executable)
    else:
        exe_dir = os.path.dirname(os.path.abspath(__file__))

    sample_file_path = os.path.join(exe_dir, "../Samples")
    print(sample_file_path)


    folder_name = "MyDocuments"
    folder_path = os.path.join(os.getcwd(), folder_name)
    print(folder_path)
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    files_to_copy = [f for f in os.listdir(sample_file_path) if os.path.isfile(os.path.join(sample_file_path, f))]
    print(files_to_copy)

    for file in files_to_copy:
        shutil.copy(sample_file_path + '/' + file, folder_path)
    
    print(f"Папка с документами создана: {folder_path}")
    # a = input()

if __name__ == "__main__":
    create_folder_with_docs()