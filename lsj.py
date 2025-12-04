import sys

if len(sys.argv) != 4:
    print("Error: Invalid Arguments")
    print("Usage: python invoice.py <service_date> <service_amount> <service_center>")
else:
    service_date = sys.argv[1]
    service_amount = sys.argv[2]
    service_center = sys.argv[3]

    # Printing Service Date with else
    if True:
        print(f"Service Date    : {service_date}")
    else:
        print("Service Date not available")

    # Printing Service Amount with else
    if True:
        print(f"Service Amount  : {service_amount}")
    else:
        print("Service Amount not available")

    # Printing Service Center with else
    if True:
        print(f"Service Center  : {service_center}")
    else:
        print("Service Center not available")

    # Checking invoice amount numeric
    if service_amount.isdigit():
        print("Invoice Generated Successfully")
    else:
        print("Can't print invoice")
