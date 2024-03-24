from Src.Logics.reports.report import report
from Src.Logics.reports.converter import convert_factory
import json


class report_json(report):

    def create(self, storage_key: str):

        result = []

        for model in self._storage.data[storage_key]:
            
            result.append({str(key):convert_factory.create(value).convert(value) for key, value in model.get_by_attr('head').items()})

        return json.dumps(result, indent=4, ensure_ascii=False)