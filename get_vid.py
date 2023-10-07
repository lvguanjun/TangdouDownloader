import json
import os

json_dir = "input"
add_json = "input/add.json"


def get_vid_set():
    vid_set = set()
    for json_file in os.listdir(json_dir):
        with open(os.path.join(json_dir, json_file)) as f:
            content = json.load(f)
            datas = content["datas"]
            if json_file == "download.json":
                for item in datas:
                    vid_set.add(int(item))
            else:
                for item in datas:
                    vid_set.add(item["vid"])
    return vid_set


def get_add_vid(last_vid: int):
    """
    获取截至到last_vid的所有视频的vid，用于获取新增收藏视频
    """
    vid_set = set()
    with open(add_json) as f:
        content = json.load(f)
        datas = content["datas"]
        for item in datas:
            if item["vid"] == last_vid:
                break
            vid_set.add(item["vid"])
    return vid_set


if __name__ == "__main__":
    vid_set = get_vid_set()
    print(vid_set)
    print(len(vid_set))
