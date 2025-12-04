import argparse
import os
import os.path as osp

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "data_path",
        type=str,
        default="./random_split_3314",
        help="Path to the NTU-RGB+D preprocessed skeleton data file",
    )
    parser.add_argument("--data_root", type=str, default=".", help="Root path to the NTU-RGB+D dataset")

    args = parser.parse_args()
    args.data_path

    dst = osp.abspath(osp.join(args.data_root, "NTU60_CS.npz"))
    src = osp.abspath(osp.join(args.data_path, "NTU60_CS.npz"))
    if osp.exists(dst):
        os.remove(dst)
    assert osp.exists(src), "Source file %s does not exist!" % src
    os.symlink(src, dst)
    print("Created symbolic link from %s to %s" % (src, dst))

    # Link ids.txt file for checking data split
    src_ids = osp.abspath(osp.join(args.data_path, "ids.txt"))
    dst_ids = osp.abspath(osp.join(args.data_root, "ids.txt"))
    if osp.exists(dst_ids):
        os.remove(dst_ids)
    assert osp.exists(src_ids), "Source file %s does not exist!" % src_ids
    os.symlink(src_ids, dst_ids)
    print("Created symbolic link from %s to %s" % (src_ids, dst_ids))
