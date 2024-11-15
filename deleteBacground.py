from PIL import Image

# Đường dẫn tới file GIF đầu vào và đầu ra
input_gif = "./output_animation1.gif"  # Cập nhật với đường dẫn chính xác của bạn
output_gif = "output_transparent1.gif"

# Mở file GIF
gif = Image.open(input_gif)
frames = []

# Xác định màu nền cần xóa (ví dụ, nếu nền gần như trắng)
background_threshold = 240  # Ngưỡng độ sáng cho nền, điều chỉnh nếu cần

# Duyệt qua từng khung hình của GIF và loại bỏ nền
for frame in range(gif.n_frames):
    gif.seek(frame)
    frame_image = gif.convert("RGBA")
    
    datas = frame_image.getdata()
    new_data = []
    
    # Loại bỏ nền dựa trên ngưỡng màu
    for item in datas:
        # Chỉ xóa những pixel có màu gần với màu trắng (nhưng không xóa trắng hoàn toàn của hình chính)
        if item[0] > background_threshold and item[1] > background_threshold and item[2] > background_threshold:
            new_data.append((255, 255, 255, 0))  # Làm trong suốt
        else:
            new_data.append(item)
    
    frame_image.putdata(new_data)
    frames.append(frame_image)

# Lưu GIF với nền trong suốt
frames[0].save(output_gif, save_all=True, append_images=frames[1:], duration=gif.info['duration'], loop=0, disposal=2, transparency=0)

print("File GIF với nền trong suốt đã được lưu.")
