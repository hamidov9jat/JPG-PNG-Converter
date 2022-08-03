def image_names(img_format: str, directory='.'):
    '''
    This is a generator which returns image names whose format is specified
    :param img_format:
    :param directory:
    :return:
    '''
    match img_format.lower():
        case 'jpg' | 'jpeg':
            image_regex = re.compile(r'^(.+)\.(jpg|jpeg)$')
        case 'png':
            image_regex = re.compile(r'^(.+)\.png$')
        case _:
            print(f'{img_format=} is not supported!')
            sys.exit(1)

    # Extract only files from the specified directory
    source = pth.Path(directory)
    files = filter(pth.Path.is_file, source.iterdir())

    # Choose only image names with the specified format
    for full_image_name in files:
        image_name = image_regex.fullmatch(full_image_name.name)
        if image_name is not None:
            yield image_name.group(1)
