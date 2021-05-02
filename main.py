from md_manager import MDManager

if __name__ == '__main__':
    mdManager = MDManager()
    file = mdManager.get_created_file()
    if file:
        mdManager.write_to_file(file)
        mdManager.complete(file)
    