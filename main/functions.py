def handle_uploaded_file(f):  
    with open('main/static/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)
    return 'main/static/'+f.name  