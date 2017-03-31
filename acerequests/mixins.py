import json


class AirportDataMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = open('data/airports.json').read()
        jsonData_loaded = json.loads(data)
        jsonDataDump = json.dumps(jsonData_loaded)
        context["jsonData"] = jsonDataDump
        return context
