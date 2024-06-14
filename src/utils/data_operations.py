import re


def to_snake_case(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def rename_columns_to_snake_case(df):
    df.columns = [to_snake_case(col) for col in df.columns]
    return df