    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    # back up code
    os.makedirs(os.path.join(save_dir, 'code'), exist_ok=True)
    os.system(' git ls-tree -r HEAD --name-only | xargs -I {} cp -a --parents {} ' + save_dir+"/code/")
