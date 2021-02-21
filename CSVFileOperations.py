import csv
#
# with open('names.csv', 'r') as csv_file:
#     csv_reader =  csv.reader(csv_file)
#
#     for item in csv_reader:
#         print(item)

#--------------------------------------------- Writing to CSV Files-------------------------------------------------#
#
# with open('names.csv', 'r') as csv_file:
#     csv_reader =  csv.reader(csv_file)
#     with open('new_names.csv', 'w') as new_file:
#         csv_writer = csv.writer(new_file, delimiter='-')
#
#         for item in csv_reader:
#             csv_writer.writerow(item)
#


#---------------------------------------------------DIctReader and DictWriter----------------------------------------#
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()  # To write header of CSV file

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)