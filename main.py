from Logics.reports.report_factory import report_factory
from Logics.start_factory import start_factory
from flask import Flask
from settings_manager import settings_manager


app = Flask(__name__)


@app.route("/api/report/<storage_key>", methods=["GET"])
def get_report(storage_key: str):
    data = start_factory().storage.data
    settings = settings_manager().settings
    if storage_key in data.keys():
        report = report_factory()
        format = settings.report_form_types
        report.create(settings, format, data).create(storage_key)
        response_type = app.response_class(
            response=report.create(settings, format, data).create(storage_key),
            status=200,
            mimetype="application/text"
        )
    else:
        response_type = app.response_class(
            status=500
        )

    return response_type


if __name__ == "__main__":
    app.run(debug=True)
