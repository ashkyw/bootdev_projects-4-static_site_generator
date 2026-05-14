import os
import sys
import shutil

def validate_directory_and_get_file_list(path):
    if os.path.exists(path):
        file_list = os.listdir(path)
        if len(file_list) == 0:
            raise Exception("Empty Directory")
        else:
            return file_list

    return f"{path} is invalid."

def remove_and_recreate_public_folder():
    public_folder = "/home/kyle/Documents/gitclones/bootdev_projects-4-static_site_generator/public/"
    shutil.rmtree(public_folder)
    os.mkdir(public_folder)

def copy_files_to_public(file_list, forcing_compliance=None):
    static_folder = "/home/kyle/Documents/gitclones/bootdev_projects-4-static_site_generator/static/"
    public_folder = "/home/kyle/Documents/gitclones/bootdev_projects-4-static_site_generator/public/"

    if len(file_list) == 0:
        return
    head, tail = os.path.split(file_list[0])
    if tail.find('.') != -1:
        tail = os.path.join(static_folder, file_list[0])
        if forcing_compliance is not None:
            tail = os.path.join(static_folder, forcing_compliance, file_list[0])
            brute, force = os.path.split(tail)
            brute_force = public_folder + '/images/'
            os.mkdir(brute_force)
            shutil.copy(tail, brute_force)
        else:
            if os.path.isfile(tail):
                shutil.copy(tail, public_folder)
                copy_files_to_public(file_list[1:])
    else:
        tail = tail + '/'
        forcing_compliance = static_folder + tail
        print(f"{forcing_compliance}")
        file = os.path.join(static_folder, tail)
        file_list = validate_directory_and_get_file_list(file)
        copy_files_to_public(file_list, forcing_compliance)

def main():
    path = "/home/kyle/Documents/gitclones/bootdev_projects-4-static_site_generator/static/"
    file_list = validate_directory_and_get_file_list(path)
    remove_and_recreate_public_folder()
    copy_files_to_public(file_list)

if __name__ == "__main__":
    main()
