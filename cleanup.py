def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} deleted successfully.")
    else:
        print(f"{filename} does not exist.")

# Example:
delete_file("github")  # ये अगर गलती से फाइल बन गई थी