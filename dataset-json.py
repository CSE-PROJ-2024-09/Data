import json


def convert_dataset_to_json(dataset):
  """Converts a dataset to JSON format.

  Args:
    dataset: A list of dictionaries, where each dictionary represents a row in the
      dataset.

  Returns:
    A JSON string representing the dataset.
  """

  json_data = []
  for row in dataset:
    json_data.append(row)

  return json.dumps(json_data)


# Example usage:

dataset = [
  
]

json_data = convert_dataset_to_json(dataset)

print(json_data)