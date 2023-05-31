class MySelectQuery:
    def __init__(self, csv_content):
        self.data = []
        lines = csv_content.strip().split('\n')
        columns = lines[0].split(',')
        for row in lines[1:]:
            values = row.split(',')
            self.data.append(dict(zip(columns, values)))

    def where(self, column_name, value):
        result = []
        for row in self.data:
            if row.get(column_name) == value:
                result.append(','.join(row.values()))
        return result
