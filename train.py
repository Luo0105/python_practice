from mmengine.runner import Runner
from mmengine.config import Config

# 从 MMACTION2 提供的默认 VideoMAEv2 配置文件加载基本结构
cfg = Config.fromfile('./configs/videomae/videomaev2_base_patch16_224_gym.py')

# 设置当前要处理的 fold（fold0、fold1、fold2）
fold = 0

# 数据集基本类型，MMACTION2 默认使用 VideoDataset 来处理帧图像组成的视频剪辑
cfg.dataset_type = 'VideoDataset'

# 设置数据路径（数据和标注文件），这两项路径是你之前生成的 txt 文件
cfg.data_root = f'dataset/clips/fold{fold}/'
cfg.ann_file_train = f'dataset/clips/fold{fold}/train_list_with_video.txt'
cfg.ann_file_val = f'dataset/clips/fold{fold}/val_list_with_video.txt'

# 配置 data 相关参数，包括 batch size 和数据读取细节
cfg.data = dict(
    videos_per_gpu=8,              # 每个 GPU 上加载的视频 clip 数量（每个 batch）
    workers_per_gpu=4,             # 每个 GPU 上的并行线程数（数据加载）
    train_dataloader=dict(
        batch_size=8,
        num_workers=4,
        dataset=dict(
            type='VideoDataset',   # 使用 VideoDataset 加载每个剪辑文件夹
            ann_file=cfg.ann_file_train,  # 指定训练数据路径列表
            data_prefix=cfg.data_root,    # clip 根目录
            filename_tmpl='{:05}.jpg',    # 文件命名模板，如 00000.jpg - 00015.jpg
            start_index=0,                # 图片编号起始索引
            modality='RGB',
            clip_len=16,                  # 每个 clip 包含 16 帧图像
            frame_interval=1,            # 帧间隔为 1（连续帧）
        ),
    ),
    val_dataloader=dict(
        batch_size=8,
        num_workers=4,
        dataset=dict(
            type='VideoDataset',
            ann_file=cfg.ann_file_val,
            data_prefix=cfg.data_root,
            filename_tmpl='{:05}.jpg',
            start_index=0,
            modality='RGB',
            clip_len=16,
            frame_interval=1,
            test_mode=True              # 启用验证模式（关闭 shuffle 等）
        ),
    )
)

# 配置模型结构：VideoMAE 的 ViT backbone + TimeSformer 分类头
cfg.model = dict(
    type='Recognizer3D',              # 表示这是一个 3D 视频分类模型
    backbone=dict(
        type='VideoMAEViT',           # 使用 VideoMAEViT 模块
        img_size=224,                 # 输入图像尺寸
        patch_size=16,                # patch 大小
        tubelet_size=2,               # 时间维度 patch 大小
        embed_dim=768,                # ViT embedding 维度
        depth=12,                     # Transformer block 深度
        num_heads=12,                 # 多头注意力数量
        drop_path_rate=0.1            # drop path（随机路径丢弃）防止过拟合
    ),
    cls_head=dict(
        type='TimeSformerHead',       # 分类头，适配 ViT 输出
        num_classes=10,               # 输出类别数量（手术阶段分类）
        in_channels=768,              # 输入通道数，必须与 ViT 输出对齐
        spatial_type='avg',           # 空间平均池化
        dropout_ratio=0.5             # dropout 防止过拟合
    ),
    data_preprocessor=dict(          # 输入数据的均值方差归一化
        type='ActionDataPreprocessor',
        mean=[123.675, 116.28, 103.53],
        std=[58.395, 57.12, 57.375]
    )
)

# 训练超参数设置
cfg.train_cfg = dict(max_epochs=50)  # 最多训练 50 个 epoch

# 优化器设置，使用 AdamW，推荐用于 transformer 模型
cfg.optim_wrapper = dict(
    optimizer=dict(
        type='AdamW',
        lr=3e-4,
        weight_decay=0.05
    ),
    clip_grad=dict(
        max_norm=40, norm_type=2      # 梯度裁剪，避免梯度爆炸
    )
)

# 日志记录相关设置
cfg.default_hooks.logger = dict(type='LoggerHook', interval=10)  # 每 10 次迭代打印一次日志
cfg.default_hooks.checkpoint = dict(interval=1, save_best='auto')  # 每个 epoch 存一次模型，并自动保存最佳
cfg.default_hooks.visualization = dict(type='LocalVisBackend')     # 可视化后端

# 添加 EarlyStopping，当 acc 超过一定时间不提升就提前停止训练
cfg.custom_hooks = [
    dict(type='EarlyStoppingHook', patience=5, metric='acc/top1', rule='greater')
]

# 设置 Visualizer，用于训练过程的可视化（loss、acc）
cfg.vis_backends = [dict(type='LocalVisBackend')]
cfg.visualizer = dict(
    type='ActionVisualizer',
    vis_backends=cfg.vis_backends
)

# 设置日志和模型保存的目录
cfg.work_dir = f'./work_dirs/videomaev2_fold{fold}'

# 初始化并开始训练
runner = Runner.from_cfg(cfg)
runner.train()
