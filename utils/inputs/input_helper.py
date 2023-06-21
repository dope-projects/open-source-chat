import os
from utils.inputs.pdf_parser import parse_pdf
from utils.inputs.markdown_parser import parse_markdown

def parse_by_file_type(input_files):
    output_files = ''
    file_type=''
    for input_file in input_files:
        file_name = input_file.name
        file_extension = os.path.splitext(file_name)[1]
        print(f"handling {file_name} with file extension {file_extension}")

        # We can accept multiple files but they have to be the same type, either pdfs or mds
        if file_extension == '.md' and file_type != 'pdf':
            file_type = 'md'
            output_files +=parse_markdown(input_file)
            
        elif file_extension == '.pdf' and file_type != 'md':
            file_type = 'pdf'
            output_files +=parse_pdf(input_file)
        else:
            raise Exception("File type was not supported!")
