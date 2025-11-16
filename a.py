from moviepy.editor import VideoFileClip, concatenate_videoclips

# Load the uploaded videos
v1 = VideoFileClip("/mnt/data/VID-20251116-WA0007.mp4")
v2 = VideoFileClip("/mnt/data/VID-20251116-WA0008.mp4")

# Trim both videos to 15 seconds each (or their full duration if shorter)
v1_cut = v1.subclip(0, min(15, v1.duration))
v2_cut = v2.subclip(0, min(15, v2.duration))

# Add a smooth crossfade transition
final = concatenate_videoclips([v1_cut, v2_cut.crossfadein(1)], method="compose")

# Ensure final duration is 30 seconds max
final = final.subclip(0, min(30, final.duration))

# Export the output video
output_path = "/mnt/data/final_reel_30s.mp4"
final.write_videofile(output_path, codec="libx264", fps=24)


