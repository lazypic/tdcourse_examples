import os
from pymediainfo import MediaInfo

media_info = MediaInfo.parse(os.getenv("HOME")+"/examples/movs/H264_1280x720_24fps.mov")
for track in media_info.tracks:
	if track.track_type == "Video":
		print "codec", track.codec_id
		print "duration", track.duration
		print "fps", track.frame_rate
		print "width", track.width
		print "height", track.height
		print "frames", int(round((float(track.duration) * float(track.frame_rate))/1000))
