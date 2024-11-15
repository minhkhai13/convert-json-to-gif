import time
import json
from selenium import webdriver
from PIL import Image
import io

# Đọc nội dung file JSON Lottie
json_path = "./Flow 4.json"  # Cập nhật đường dẫn nếu cần
with open(json_path, 'r') as file:
    lottie_json = json.load(file)

# Khởi tạo Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

# Mở trang trống
driver.get("data:text/html,<html><head><title>Lottie Animation</title></head><body></body></html>")

# Thêm script lottie-web từ CDN vào trang
driver.execute_script('''
    var script = document.createElement('script');
    script.src = 'https://cdnjs.cloudflare.com/ajax/libs/lottie-web/5.7.4/lottie.min.js';
    document.head.appendChild(script);
''')

# Đợi một chút để script lottie-web được tải
time.sleep(2)

# Inject JSON vào trang và render
driver.execute_script('''
    const lottieData = arguments[0];
    const animationContainer = document.createElement('div');
    animationContainer.id = 'animation';
    animationContainer.style.width = '1000px';
    animationContainer.style.height = '1000px';
    document.body.appendChild(animationContainer);

    window.lottie.loadAnimation({
        container: document.getElementById('animation'),
        renderer: 'svg',
        loop: true,
        autoplay: true,
        animationData: lottieData
    });
''', lottie_json)

# Đợi animation render
time.sleep(2)

# Tạo danh sách lưu khung hình
frames = []
duration = 0.1  # thời gian mỗi frame, tính bằng giây

# Chụp lại từng khung hình
for i in range(112):  # lấy 60 khung hình
    png = driver.get_screenshot_as_png()
    image = Image.open(io.BytesIO(png))
    frames.append(image)
    time.sleep(duration)

# Lưu các khung hình thành GIF
frames[0].save("output_animation1.gif", save_all=True, append_images=frames[1:], duration=int(duration * 1000), loop=0)

print("File GIF đã được lưu thành công.")
driver.quit()
