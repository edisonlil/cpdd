import os
import shutil
import chardet
def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

def rename_and_replace_in_file(source_directory, target_directory, old_char, new_char):
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            old_file_path = os.path.join(root, file)
            new_file_name = old_file_path.replace(old_char, new_char)
            new_file_path = os.path.join(target_directory, new_file_name)

            # 创建目标目录（如果不存在）
            if not os.path.exists(os.path.dirname(new_file_path)):
                os.makedirs(os.path.dirname(new_file_path))

            # 自动检测文件的编码并读取内容
            encoding = detect_encoding(old_file_path)
            try:
                with open(old_file_path, 'r', encoding=encoding) as f:
                    file_data = f.read()
            except UnicodeDecodeError:
                print(f"Skipped decoding file: {old_file_path}")
                continue

            # 修改文件内容
            new_file_data = file_data.replace(old_char, new_char)

            # 将修改后的内容写入新文件
            with open(new_file_path, 'w', encoding='utf-8') as f:
                f.write(new_file_data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # 使用函数
    rename_and_replace_in_file(r'D:\tmp\greatbay-framework', r'D:\tmp\gonline-framework', 'greatbay',
                               'gonline')


