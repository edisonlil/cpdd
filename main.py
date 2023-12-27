import argparse
import os
import shutil
import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

def rename_and_replace_in_file(source_directory, target_directory, char_map):
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            old_file_path = os.path.join(root, file)
            new_file_name = old_file_path
            for old_char, new_char in char_map.items():
                new_file_name = new_file_name.replace(old_char, new_char)
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
            new_file_data = file_data
            for old_char, new_char in char_map.items():
                new_file_data = new_file_data.replace(old_char, new_char)

            # 将修改后的内容写入新文件
            with open(new_file_path, 'w', encoding='utf-8') as f:
                f.write(new_file_data)
def cpdd_cli():
    parser = argparse.ArgumentParser(
        description='Copy Deep Designate - A tool for deep copying a project and designating a new project code.')

    parser.add_argument('-d', '--char-mapping', type=str, required=True,
                        help='A comma-separated list of target:source character mappings, e.g., "targetChars:sourceChars,targetChars:sourceChars"')

    parser.add_argument('-o', '--output-path', type=str, required=True,
                        help='The path to the output directory where the cloned project will be saved.')

    parser.add_argument('source_path', type=str, nargs='?', default=None,
                        help='The path to the source project. If not provided, assumes the current directory.')
    args = parser.parse_args()


    if args.source_path is None:
       assert args.source_path is None, 'You must specify the source path'

    char_mapping_list = args.char_mapping.split(',')
    char_map = {}
    for mapping in char_mapping_list:
        target_chars, source_chars = mapping.split(':')
        char_map[target_chars] = source_chars


    rename_and_replace_in_file(args.source_path, args.output_path, char_map)


def test():
    # 使用函数
    char_map = {'aaa': 'bbb', 'Aaa': 'Bbb'}
    rename_and_replace_in_file(r'D:\tmp\sourceProject', r'D:\tmp\outputProject', char_map)
    pass

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cpdd_cli()
pass


