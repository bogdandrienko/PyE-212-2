def print_data_from_frontend(request, method="GET"):
    print(f"\nGET {request.GET}")
    print(f"POST {request.POST}")
    print(f"FILES {request.FILES}\n")
