import pandas as pd
import subprocess
input_file = "C:\\Users\\user\\python\\EXCEL\\data_arrange\\original_a_b.csv"
output_file = "C:\\Users\\user\\python\\EXCEL\\data_arrange\\converted_a_b.csv"
df = pd.read_csv(input_file)
# a列とb列を組み合わせてフィルタリングしたデータを格納
dataframes = []
a_values = df['a'].unique()
b_values = df['b'].unique()
for a_value in a_values:
    for b_value in b_values:
        filtered_df = df[(df['a'] == a_value) & (df['b'] == b_value)].copy()
                # 値が存在する場合のみデータフレームを作成
        if not filtered_df.empty:
            filtered_df.rename(columns={'y': f'a_{a_value}_b_{b_value}'}, inplace=True)
            filtered_df.drop(['a', 'b'], axis=1, inplace=True)  # 不要な列を削除
            dataframes.append(filtered_df)
if dataframes:
    merged_df = dataframes[0]
    for i in range(1, len(dataframes)):
        merged_df = pd.merge(merged_df, dataframes[i], on='x')
else:
    merged_df = pd.DataFrame()
# 結果をCSVファイルとして出力
merged_df.to_csv(output_file, index=False)
# ファイルを開く
subprocess.Popen(["start", "", output_file], shell=True)