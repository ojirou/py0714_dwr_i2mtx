import pandas as pd
import subprocess
input_file = "C:\\Users\\user\\python\\EXCEL\\data_arrange\\original.csv"
output_file = "C:\\Users\\user\\python\\EXCEL\\data_arrange\\converted.csv"
# CSVファイルの読み込み
df = pd.read_csv(input_file)
# df.head()
# x列の値をn回繰り返す新しい列を作成
n = 10
# n = len(df['x'])
m = int(len(df) / n)
df['x_repeat'] = df['x']
# 元のデータフレームの行数
original_rows = len(df)
# 新しいDataFrameを作成
new_df = pd.DataFrame({'x': df['x_repeat']})
# 新しいデータフレームの行数
new_rows = len(new_df)
# 新しい行数を1/3にする
desired_rows = original_rows // 3
# 行を削除して新しいデータフレームの行数を1/3にする
if new_rows > desired_rows:
    drop_indices = new_df.index[desired_rows:]
    new_df = new_df.drop(drop_indices)
# y列をm回繰り返し、y1、y2、...の列を作成
for i in range(1, m + 1):
    y_column_name = 'y{}'.format(i)
    new_df[y_column_name] = df['y'].values[(i - 1) * n:i * n]
# 変換結果をCSVファイルとして出力
new_df.to_csv(output_file, index=False)
subprocess.Popen(["start", "", output_file], shell=True)