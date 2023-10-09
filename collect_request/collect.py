import requests

base_url = "https://aa.tangdou.com:12308/api.php"

base_params = {
    "mod": "fav",
    "ac": "lists",
    "anon_id": "f9976017425e10f22cbd2d7f7d73e0aa",
    "bucketlist": "play_page_head_ad-old%2Cdownload_video_ad-old%2Cplay_page_multi_head_ad-new1%2Cdownpage_feed-new%2Ctop_search-new%2Cdownload_ad_head-new%2Cdownload_ad_tail-new%2Cfeed_plaque_ad-new2%2Cpause_ad_ui-old%2Cplaypage_plaque_ad-old%2Cplaypage_plaque_ad_new-old_equal%2Cfeed_plaque_ad_ios-new%2Cpush_open-new%2Csend_revision-new%2Chome_add_mp3-new%2C0%2Cvideo_play_share-new%2Cmember_block-new2%2Cvip_tab_change-new%2Cranklist_entrance_exp-new1%2Cplaypage_danceteach-new%2Cvip_series_course-old%2Cplayer_packing-old%2Cmy_tab_ui-new1%2Cpractice_room-old%2Cdownpage_slide_photo-new%2Cslow_play_function-old%2Cmirror_optimization-new%2Cfav_popup-old%2Cdance_share_inapp-old_equal",
    "build": "1",
    "client": "1",
    "devices": "iPhone9%2C2",
    "dic": "appstore",
    "diu": "3A25E89A-B3FE-4FF3-821F-A782237DF324",
    "diu2": "",
    "diu3": "B62699B4-BC5D-4AE2-96BC-C14D3FC787EB",
    "diu5": "c51b6d59fa3cec27d0f8d31630003646",
    "div": "8.1.9",
    "gtcid": "ca27bef555397f65617a299494dc4e40",
    "height": "667",
    "package": "com.dreamwindows.video",
    "page": "1",
    "query": "",
    "sdkversion": "14.8",
    "signdate": "1695950708861",
    "smallvideo": "1",
    "startid": "245022309",
    "stepid": "6",
    "suid": "12709089",
    "time": "1696599924052",
    "token": "8c537fdbfc37ba77848bab5579c80898",
    "uid": "12709089",
    "uuid": "921360956476845018e7b6edf45786d1",
    "ver": "v2",
    "version": "8.1.9",
    "width": "375",
    "xinge": "e27026fb68863c0c2e0749d36c6fb1150f34c020310f6ad5c0958d375dd19f68",
    "hash": "5dfd127eb6060b4a0f4ba466b4d62e79",
}


def get_collect(update_params: dict = None):
    params = base_params.copy()
    if update_params:
        for k, v in update_params.items():
            params[k] = v
    url = base_url + "?" + "&".join([f"{k}={v}" for k, v in params.items()])
    resp = requests.get(url=url)
    if resp.status_code == 200:
        return resp.json()
    else:
        raise RuntimeError("get collect error, error page:", params["page"])


if __name__ == "__main__":
    update_params = {
        "page": 3,
        "startid": 245085924,
        "stepid": 72,
        "time": 1696663747008,
        "hash": "71658aab80dd3fff8d673e609f565277",
    }
    res = get_collect(update_params)
    print(type(res))
