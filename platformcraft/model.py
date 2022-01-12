class AuthInfo:
    def __init__(self, data):
        self.user_id = data["user_id"]
        self.owner_id = data["owner_id"]
        self.expires_at = data["expires_at"]


class UploadInfo:
    def __init__(self, data):
        self.id = data["id"]
        self.is_dir = data["is_dir"]
        self.type = data["type"]
        self.status = data["status"]
        self.name = data["name"]
        self.path = ["path"]
        self.size = data["size"]
        self.content_type = data["content_type"]
        self.description = data["description"]
        self.create_time = ["create_time"]
        self.change_time = data["change_time"]
        self.create_time = data["create_date"]
        self.latest_update = ["latest_update"]
        self.private = data["private"]

        # "advanced":{"video_streams":[{"index":0,
        #                            "codec_type":"video",
        #                            "codec_name":"h264",
        #                            "codec_long_name bson:":"H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10","duration":126.026026,"bit_rate":1431912,"display_aspect_ratio":"355:184","width":710,"height":368,"fps":29.97}],
        #          "audio_streams":[{"index":1,
        #                            "codec_type":"audio",
        #                            "codec_name":"aac",
        #                            "codec_long_name":"AAC (Advanced Audio Coding)",
        #                            "duration":126.026021,"bit_rate":61398,
        #                            "sample_rate":48000,"channels":2,
        #                            "channel_layout":"stereo",
        #                            "language":"eng"}],
        #          "subtitle_streams":null,
        #          "format":{"nb_streams":2,
        #                    "format_name":"mov,mp4,m4a,3gp,3g2,mj2",
        #                    "format_long_name":"QuickTime / MOV",
        #                    "duration":126.08,"bit_rate":1495934}},
        # self.preview_url = data["preview_url"]
        # self.previews = data["previews"]
        # self.download_url = ["download_url"]
        # self.hls = data["hls"]
        # self.perms = data["perms"]
        # self.etag = data["etag"]
