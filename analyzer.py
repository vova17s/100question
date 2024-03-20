import pandas as pd


def read_question():
    xls = pd.ExcelFile('_100 вопросов мастеру.xlsx')
    data_frame_dict = {}
    for sheet_name in xls.sheet_names:
        data_frame_dict[sheet_name] = pd.read_excel(xls, sheet_name, index_col=0).dropna()
    return data_frame_dict

data = read_question()

def get_sample_and_delete(sheet_name, data_frame_dict):
    sample_obj = data_frame_dict[sheet_name].sample()
    data_frame_dict[sheet_name].drop(sample_obj.index, inplace=True)
    count_question = len(data_frame_dict[sheet_name].index)
    if count_question == 0:
        del data_frame_dict[sheet_name]
    return sample_obj, count_question
