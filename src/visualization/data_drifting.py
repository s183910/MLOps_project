# from evidently.metric_preset import DataDriftPreset


import pandas as pd


from evidently.test_suite import TestSuite
from evidently.test_preset import DataStabilityTestPreset


data_frame = pd.read_csv("data/raw/sign_mnist_train.csv")
# transpose the dataframe
data_frame = data_frame.transpose()


data_stability = TestSuite(
    tests=[
        DataStabilityTestPreset(),
    ]
)
data_stability.run(
    current_data=data_frame.iloc[:300], reference_data=data_frame.iloc[300:], column_mapping=None
)
data_stability.save_html("DataStability.html")
# with open("DataDrifting.html", "r", encoding="utf-8") as f:
#     html_content = f.read()


# from evidently.report import Report
# from evidently.metric_preset import DataDriftPreset

# report = Report(metrics=[DataDriftPreset()])
# report.run(reference_data=data_frame.iloc[391:], current_data=data_frame.iloc[:391])
# report.save_html("DDReport.html")

# with open("DDReport.html", "r", encoding="utf-8") as f:
#     html_content = f.read()


# ________________________  Data Quality ________________________
# from evidently.test_suite import TestSuite
# from evidently.tests import TestNumberOfMissingValues

# data_test = TestSuite(tests=[TestNumberOfMissingValues()])
# data_test.run(reference_data=data_frame.iloc[391:], current_data=data_frame.iloc[:391])
