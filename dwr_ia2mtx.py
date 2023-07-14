import pandas as pd
import subprocess
input_file = "C:\\Users\\user\\python\\EXCEL\\data_arrange\\original_a.csv"
output_file = "C:\\Users\\user\\python\\EXCEL\\data_arrange\\converted_a.csv"
df = pd.read_csv(input_file)
# a列を新たに作成し、各要素にフィルタリングしたデータを格納
dataframes = []
a_values = df['a'].unique()
for a_value in a_values:
    filtered_df = df[df['a'] == a_value].copy()
    filtered_df.rename(columns={'y': f'a_{a_value}'}, inplace=True)
    filtered_df.drop('a', axis=1, inplace=True)  # a列を削除
    dataframes.append(filtered_df)
# x列をキーにしてデータフレームを結合
merged_df = dataframes[0]
for i in range(1, len(dataframes)):
    merged_df = pd.merge(merged_df, dataframes[i], on='x')
# 結果をCSVファイルとして出力
merged_df.to_csv(output_file, index=False)
subprocess.Popen(["start", "", output_file], shell=True)