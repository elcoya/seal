"""

@author: anibal

"""

class CsvTuplePrinter:
    """
    Helper class to handle the writing of tuples as comma separated lines to a given file.
    """
    
    output_file = None
    
    def __init__(self, output_file_name=None):
        if output_file_name is None:
            self.output_file = None
        else:
            self.output_file = open(output_file_name, "w")
    
    def open(self, output_file_name):
        if self.output_file is not None:
            self.output_file.close()
        self.output_file = open(output_file_name, "w")
    
    def put(self, tuple_to_write):
        stringified_tuple = ",".join(str(field) for field in tuple_to_write)
        self.output_file.write(stringified_tuple + "\n")
    
    def close(self):
        if self.output_file is not None:
            self.output_file.close()
