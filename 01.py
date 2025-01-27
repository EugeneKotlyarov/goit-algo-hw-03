import os
import shutil
import argparse


# використовуємо argparse для збирання аргументів
# використовуємо тільки обов'язкові аргументи
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("src", help="Path to the source directory.")
    parser.add_argument("dst", help="Path to the destination directory")
    return parser.parse_args()


# 1. пошут вихідної директорії та її створення за потреби
# 2.1 ітеративно запускаємо функцію, якщо зноходимо катлог всередині
# 2.2 інакше копіюємо файл
# 3 обробка виключень, якщо файл неможливо скопіювати


def copy_and_sort_files(src, dst):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        src_item = os.path.join(src, item)
        if os.path.isdir(src_item):
            copy_and_sort_files(src_item, dst)
        elif os.path.isfile(src_item):
            try:
                file_ext = os.path.splitext(item)[1].lstrip(".").lower()

                if not file_ext:
                    file_ext = "no_extension"
                dst_path = os.path.join(dst, file_ext)

                if not os.path.exists(dst_path):
                    os.makedirs(dst_path)

                shutil.copy2(src_item, dst_path)

            except Exception as e:
                print(f"Помилка при копіюванні {src_item}: {e}")


def main():
    args = parse_arguments()
    src = args.src
    dst = args.dst

    if not os.path.exists(src):
        print(f"Вхідний каталог '{src}' не існує")
        return

    copy_and_sort_files(src, dst)
    print(f"Файли скопійовано з '{src}' до '{dst}'")


if __name__ == "__main__":
    main()
