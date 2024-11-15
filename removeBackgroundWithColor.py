from PIL import Image

# Đường dẫn tới file GIF đầu vào và đầu ra
input_gif = "./output_animation1.gif"  # Cập nhật với đường dẫn chính xác của bạn
output_gif = "output_transparent1.gif"

# Mã màu nền và độ dung sai
background_color = (0,255,26)  # Mã màu nền (cập nhật nếu cần)
tolerance = 20  # Độ dung sai, bạn có thể điều chỉnh để có viền mượt hơn

# Mở file GIF
gif = Image.open(input_gif)
frames = []

# Duyệt qua từng khung hình của GIF và loại bỏ nền với tolerance
for frame in range(gif.n_frames):
    gif.seek(frame)
    frame_image = gif.convert("RGBA")
    
    datas = frame_image.getdata()
    new_data = []
    
    # Loại bỏ nền dựa trên mã màu với độ dung sai
    for item in datas:
        # Kiểm tra nếu pixel gần giống với mã màu nền trong khoảng tolerance
        if all(abs(item[i] - background_color[i]) <= tolerance for i in range(3)):
            new_data.append((255, 255, 255, 0))  # Làm trong suốt
        else:
            new_data.append(item)
    
    frame_image.putdata(new_data)
    frames.append(frame_image)

# Lưu GIF với nền trong suốt và viền mượt hơn
frames[0].save(output_gif, save_all=True, append_images=frames[1:], duration=gif.info['duration'], loop=0, disposal=2, transparency=0)

print("File GIF với nền trong suốt và viền mượt đã được lưu.")
