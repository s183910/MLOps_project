from evidently.report import Report
from evidently.metric_preset import DataDriftPreset
import pandas as pd
from sklearn import datasets


reference_data = datasets.load_iris(as_frame='auto').frame

current_data = pd.read_csv('prediction_database.csv')

# report = Report(metrics=[DataDriftPreset()])
# report.run(reference_data=reference, current_data=current)
# report.save_html('report.html')


# from evidently.metric_preset import DataDriftPreset, DataQualityPreset
# report = Report(metrics=[DataDriftPreset(), DataQualityPreset()])
