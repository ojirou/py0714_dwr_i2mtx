import pandas as pd
import subprocess
base_folder= "C:\\Users\\user\\python\\EXCEL\\data_arrange\\"
file_name="original_a"
input_file = base_folder+file_name+".csv"
output_file = base_folder+file_name+"_r.csv"
df = pd.read_csv(input_file)
# a列を新たに作成し、各要素にフィルタリングしたデータを格納
aaaaa="a"
xxxxx="x"
yyyyy="y"
dataframes = []
a_values = df['a'].unique()
for a_value in a_values:
    filtered_df = df[df[aaaaa] == a_value].copy()
    filtered_df.rename(columns={yyyyy: f'a_{a_value}'}, inplace=True)
    filtered_df.drop(aaaaa, axis=1, inplace=True)  # a列を削除
    dataframes.append(filtered_df)
# x列をキーにしてデータフレームを結合
merged_df = dataframes[0]
for i in range(1, len(dataframes)):
    merged_df = pd.merge(merged_df, dataframes[i], on=xxxxx)
# 結果をCSVファイルとして出力
merged_df.to_csv(output_file, index=False)
subprocess.Popen(["start", "", output_file], shell=True)