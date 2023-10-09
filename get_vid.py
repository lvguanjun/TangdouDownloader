from collect_request.collect import get_collect


def get_vid_set(last_vid=None):
    # 抓包获取的收藏请求参数
    update_params = [
        {},
        {
            "page": 2,
            "startid": 245084409,
            "stepid": 61,
            "hash": "3d46287bdc874028c5717addc6b059ea",
            "time": 1696662051829,
        },
        {
            "page": 3,
            "startid": 245085924,
            "stepid": 72,
            "hash": "71658aab80dd3fff8d673e609f565277",
            "time": 1696663747008,
        },
    ]
    vid_set = set()
    if not last_vid:
        for params in update_params:
            res = get_collect(params)
            for item in res["datas"]:
                vid_set.add(item["vid"])
    else:
        for params in update_params:
            res = get_collect(params)
            for item in res["datas"]:
                if item["vid"] == last_vid:
                    return vid_set
                vid_set.add(item["vid"])
    return vid_set


if __name__ == "__main__":
    vid_set = get_vid_set(20000003062981)
    print(vid_set)
    print(len(vid_set))
    vid_set = get_vid_set()
    print(len(vid_set))