from Src.Logics.reports.report import report


class report_csv(report):

    def create(self, storage_key: str):

        result = []
        headers = self._storage.data[storage_key][0].get_attr_keys('head')
        result.append(';'.join(headers))

        for model in self._storage.data[storage_key]:

            result.append(';'.join(map(str, model.get_attr_values('head'))))
            
        return '\n'.join(result)