def reset(files):
    '''Supply list of files
    For each file, fill with empty '''
    print('Resetting.....')
    for file in files:
        with open(file,'w') as f:
            f.write('')
    print('Done')
