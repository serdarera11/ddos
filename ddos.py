import requests
import threading

def send_request(url):
    try:
        response = requests.get(url)
        print(f"İstek gönderildi -> {response.status_code}")
    except requests.exceptions.RequestException:
        print("Bağlantı hatası!")

# Kullanıcıdan giriş al
site = input("Test edilecek site URL'sini girin (http/https ile): ")
num_requests = int(input("Kaç istek göndermek istiyorsun?: "))

# Thread'leri başlat
threads = []
for i in range(num_requests):
    thread = threading.Thread(target=send_request, args=(site,))
    threads.append(thread)
    thread.start()

# Tüm thread'lerin tamamlanmasını bekle
for thread in threads:
    thread.join()

print(f"{num_requests} istek tamamlandı!")
