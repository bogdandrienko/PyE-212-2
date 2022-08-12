def print_data_from_frontend(request, method="GET"):
    print(f"GET {request.GET}\n")
    print(f"POST {request.POST}\n")
    print(f"FILES {request.FILES}\n")
