def get_file(file_obj):
    f_name = file_obj.filename    
    file_obj.save(f_name)
    file = open(f_name,'r')
    return f_name


