def test_func():
    print("hello world")


def clone_colab_sheet(repository):
    from google.colab import drive
    import os
    import subprocess
    import shutil
    from datetime import datetime
    from IPython.display import display, Markdown

    # Extract repo name from URL
    repo_name = repository.rstrip('/').split('/')[-1]

    # Mount Google Drive
    drive.mount('/content/drive')

    # Set paths
    base_dir = '/content/drive/MyDrive'
    repo_path = os.path.join(base_dir, repo_name)
    os.chdir(base_dir)

    # Backup existing repo if it exists
    if os.path.exists(repo_path):
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        backup_dir = f"{repo_name}_backup_{timestamp}"
        backup_path = os.path.join(base_dir, backup_dir)

        print(f"⚠️ Repository '{repo_name}' already exists. Backing up to '{backup_dir}' before overwriting...")
        shutil.move(repo_path, backup_path)

    # Clone fresh copy of the repository
    print(f"⬇️ Cloning repository '{repo_name}'...")
    subprocess.run(['git', 'clone', repository])

    # Change directory to the repo
    os.chdir(repo_path)

    # Display message with instructions
    display(Markdown(f"""
✅ **Repository '{repo_name}' has been cloned successfully.**  
📁 To access the files, go to [**drive.google.com**](https://drive.google.com), open **My Drive**, and look for the folder named **`{repo_name}`**.
    """))
