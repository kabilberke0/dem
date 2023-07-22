import time

def login_to_instagram(username, password):
    # Instagram'a giriş yapmak için gerekli işlemleri burada gerçekleştirin.
    # Bu işlem için requests kütüphanesini veya Instagram'ın web arayüzünü kullanabilirsiniz.
    # Oturum açma başarılı olursa oturum açtığınız kullanıcıyı temsil eden bir oturum nesnesi döndürün.

def upload_video_to_instagram(video_path, caption):
    # Belirtilen videoyu Instagram'a yüklemek için gerekli işlemleri burada gerçekleştirin.
    # Bu işlem için requests kütüphanesini veya Instagram'ın web arayüzünü kullanabilirsiniz.
    # Yükleme başarılı olursa True, aksi halde False döndürün.

def main():
    # Kullanıcı adı ve şifre bilgilerinizi burada girin.
    username = "kabilberke5@gmail.com"
    password = "Kabil5353"

    # Her gün paylaşılacak videoların dosya yollarını içeren bir liste oluşturun.
    videos_to_share = [
        "çıkağr.mp4",
      
        # Burada diğer videoları ekleyin...
    ]

    # Instagram'a giriş yapın
    session = login_to_instagram(username, password)

    # Gün sayacını başlatın
    day_count = 1

    # Her gün için bir döngü oluşturun
    for video_path in videos_to_share:
        caption = f"Gün {day_count} çıkağr"  # Açıklama kısmına gün numarasını ekleyin

        upload_success = upload_video_to_instagram(video_path, caption)

        if upload_success:
            print(f"Video '{video_path}' başarıyla paylaşıldı.")
        else:
            print(f"Hata! Video '{video_path}' paylaşılamadı.")

        # Bir sonraki gün için bekleyin (24 saat = 86400 saniye)
        time.sleep(86400)

        # Gün sayacını bir artırın
        day_count += 1

if __name__ == "__main__":
    main()