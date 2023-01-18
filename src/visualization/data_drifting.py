import pandas as pd
from evidently.test_suite import TestSuite
from evidently.test_preset import DataStabilityTestPreset
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

image = pd.read_csv("data/raw/sign_mnist_train.csv")

avearege_brightness = image.mean(axis=1)
max_value = image.max(axis=1)
min_value = image.min(axis=1)
contrast = max_value - min_value

# Join the avearege_brightness, max_value, min_value, contrast into a single dataframe
data_frame = pd.concat([avearege_brightness, max_value, min_value, contrast], axis=1)


data_stability = TestSuite(
    tests=[
        DataStabilityTestPreset(),
    ]
)
data_stability.run(
    current_data=data_frame.iloc[:391], reference_data=data_frame.iloc[391:], column_mapping=None
)
data_stability.save_html("src/visualization/DataStability.html")


report = Report(metrics=[DataDriftPreset()])
report.run(reference_data=data_frame.iloc[391:], current_data=data_frame.iloc[:391])
report.save_html("src/visualization/DataDriftingReport.html")
