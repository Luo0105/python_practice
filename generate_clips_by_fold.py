import os
import json
import shutil

def make_dir(path):
    """
    如果目录不存在就创建，防止后续写文件失败。
    """
    if not os.path.exists(path):
        os.makedirs(path)

def copy_clip(img_paths, label, output_dir, clip_idx):
    """
    将一个 clip（由16帧图像组成）复制到指定的输出目录，并命名为 clip_00000 这样的格式。

    参数：
        img_paths: 当前 clip 包含的图像路径列表
        label: 当前 clip 的分类标签（如阶段编号）
        output_dir: 输出 clip 所在的 train/val 文件夹
        clip_idx: clip 的编号（用于命名）

    返回：
        clip_dir: 该 clip 所在的目录路径
        label: 分类标签
    """
    clip_dir = os.path.join(output_dir, f'clip_{clip_idx:05d}')
    os.makedirs(clip_dir, exist_ok=True)  # 创建 clip 文件夹
    for i, img_path in enumerate(img_paths):
        # 将原始图像复制到新的 clip 目录，重命名为 00000.jpg ~ 00015.jpg
        shutil.copyfile(img_path, os.path.join(clip_dir, f'{i:05d}.jpg'))
    return clip_dir, label

def process_fold(fold_idx, fold_info_dir, dataset_root, output_root, clip_len):
    """
    处理某一个 fold（fold0 / fold1 / fold2）：
    - 加载 json 文件中该 fold 的训练和验证图像路径
    - 按类别连续采 clip（长度为16的帧），只保留同一类的
    - 保存为 clip，并记录生成的 list 文件

    参数：
        fold_idx: 当前 fold 编号
        fold_info_dir: 存放 fold json 文件的目录
        dataset_root: 原始图像数据所在的根目录
        output_root: 输出的 clip 数据根目录
        clip_len: 每个 clip 的帧数（默认16）
    """
    print(f'Processing fold{fold_idx}...')

    # 加载该 fold 的 json 文件，如 data_info_fold0.json
    fold_json_path = os.path.join(fold_info_dir, 'json', f'data_info_fold{fold_idx}.json')
    with open(fold_json_path, 'r') as f:
        fold_data = json.load(f)

    # 分别处理 train 和 val 两部分数据
    for phase in ['train', 'val']:
        img_paths = fold_data[phase]['img']       # 图像路径列表
        labels = fold_data[phase]['phase']        # 每张图对应的分类标签

        assert len(img_paths) == len(labels), "图像数量和标签数量不一致"

        output_dir = os.path.join(output_root, f'fold{fold_idx}', phase)
        make_dir(output_dir)  # 创建输出目录

        clip_records = []  # 保存 (clip路径, 标签) 以生成 list.txt

        # 开始组装 clip
        current_clip = []
        current_label = []
        clip_idx = 0

        for img_path, label in zip(img_paths, labels):
            current_clip.append(img_path)
            current_label.append(label)

            if len(current_clip) == clip_len:
                # 只有当 16 张图都是同一类时，才认为是一个有效 clip
                if all(l == current_label[0] for l in current_label):
                    clip_dir, label_id = copy_clip(current_clip, current_label[0], output_dir, clip_idx)
                    # 相对路径写入 list.txt 文件
                    rel_path = os.path.relpath(clip_dir, output_root).replace("\\", "/")
                    clip_records.append((rel_path, label_id))
                    clip_idx += 1

                # 无论是否有效 clip，都重置窗口
                current_clip = []
                current_label = []

        # 写入 list.txt 文件（VideoDataset 或训练脚本使用）
        list_txt_path = os.path.join(output_root, f'fold{fold_idx}', f'{phase}_list.txt')
        with open(list_txt_path, 'w') as f:
            for rel_path, label_id in clip_records:
                f.write(f"{rel_path} {label_id}\n")

        print(f'{phase} fold{fold_idx} 完成！ 生成了 {clip_idx} 个clips。')

def main():
    # 设置路径（根据你的目录结构进行修改）
    fold_info_dir = '/win/scallop/user/luo/Kaggle/2025/dataset/fold_info'   # 存放 JSON 的目录
    dataset_root = '/win/scallop/user/luo/Kaggle/2025/dataset/train'        # 原始图片序列目录
    output_root = '/win/scallop/user/luo/Kaggle/2025/dataset/clips'         # 输出 clips 的地方
    clip_len = 16  # 每个 clip 包含的帧数

    make_dir(output_root)

    for fold_idx in range(3):  # 批量处理 fold0, fold1, fold2
        process_fold(fold_idx, fold_info_dir, dataset_root, output_root, clip_len)

if __name__ == '__main__':
    main()
