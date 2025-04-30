import os


# 功能：将已有的 clip list txt 文件中的 clip 路径，拼接成完整的视频 clip 路径，并重新写入一个新 txt 文件
# 原始 txt 文件内容：clip 相对路径（如 fold0/train/clip_00000）+ label
# 新 txt 文件内容：video 路径（clip 文件夹路径） + label（用于 VideoDataset 加载）

def convert_list_with_video(txt_path, output_path, root_dir):
    """
    参数：
        txt_path: 原始 clip list 文件路径，如 train_list.txt
        output_path: 输出新 txt 路径
        root_dir: 所有 clip 的根目录（绝对路径或相对路径）
    """

    with open(txt_path, 'r') as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        line = line.strip()
        if not line:
            continue  # 跳过空行

        # 每一行格式如：fold0/train/clip_00000 3
        rel_path, label = line.split()

        # 将相对路径拼接为完整视频路径
        # 例如：dataset/clips/fold0/train/clip_00000
        video_path = os.path.join(root_dir, rel_path)

        # 保持路径风格统一为 Linux 风格（避免 Windows 路径分隔符）
        video_path = video_path.replace('\\', '/')

        # 保存为新的一行：视频路径 + 标签
        new_lines.append(f"{video_path} {label}\n")

    # 将新内容写入 output_path
    with open(output_path, 'w') as f:
        f.writelines(new_lines)

    print(f'转换完成：共处理 {len(new_lines)} 条记录。新文件保存至 {output_path}')


if __name__ == '__main__':
    # 要转换的 fold 编号（可以循环做多个 fold）
    fold = 0

    # 根路径：指向 clips 文件夹
    root_dir = f'dataset/clips/fold{fold}'

    # 原始 txt 路径（之前生成的 train 和 val list）
    txt_train = f'dataset/clips/fold{fold}/train_list.txt'
    txt_val = f'dataset/clips/fold{fold}/val_list.txt'

    # 输出新的带 video 路径的 txt（将用于 VideoDataset）
    output_train = f'dataset/clips/fold{fold}/train_list_with_video.txt'
    output_val = f'dataset/clips/fold{fold}/val_list_with_video.txt'

    # 分别转换 train 和 val 文件
    convert_list_with_video(txt_train, output_train, root_dir)
    convert_list_with_video(txt_val, output_val, root_dir)
