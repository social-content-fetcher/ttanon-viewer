# ttanon-viewer: anonim TikTok izleyici istemcisi

**ttanon-viewer**, anonim TikTok izleyicisi **[TTAnon](https://ttanon.com)** için küçük bir Python paketi ve komut
satırı aracıdır. Herhangi bir TikTok bağlantısını, `@kullanıcıadı`'nı ya da `#hashtag`'i TTAnon sayfasına çevirir;
böylece **TikTok'u hesap açmadan**, uygulamasız ve giriş yapmadan izleyebilirsiniz.

> Bir TikTok profiline hemen bakmak mı istiyorsunuz? Bu pakete gerek yok: **[ttanon.com](https://ttanon.com)**'u açın
> ya da herhangi bir TikTok bağlantısında `tiktok.com` yerine `ttanon.com` yazın.

```text
https://www.tiktok.com/@khaby.lame/video/7212345678901234567
https://ttanon.com/@khaby.lame/video/7212345678901234567
```

## TTAnon nedir?

[TTAnon](https://ttanon.com), herkese açık TikTok içeriğini her tarayıcıda anonim olarak izlemek için ücretsiz,
bağımsız bir sitedir. TikTok'un adres yapısını aynen kullanır: profiller (`/@kullanıcı`), videolar
(`/@kullanıcı/video/ID`), fotoğraf gönderileri, hashtag'ler (`/tag/ad`), sesler (`/music/başlık-ID`), konular
(`/discover/konu`), arama ve [trendler](https://ttanon.com/trending).

- **Hesap yok, uygulama yok, giriş yok.** İzledikleriniz bir TikTok hesabının izleme geçmişine düşmez.
- **TikTok betikleri yok.** Sayfayı TTAnon'un sunucusu alır ve size düz HTML gönderir; TikTok'un betikleri, pikselleri
  ve izleyicileri TTAnon sayfalarında hiç yüklenmez. (Oynat'a bastığınızda video dosyası TikTok'un video
  sunucularından gelir: [Ne kadar anonim?](https://ttanon.com/about#anonymous))
- **Video indirme:** içerik üreticisi izin veriyorsa MP4 olarak.
- **Zengin video bilgisi:** TikTok sağlıyorsa metin dökümü, kategori, konum, dil, süre, çözünürlük, sesin albümü ve
  Spotify / Apple Music bağlantıları, düet / stitch / indirme ayarları.
- **Profil araçları:** yüklenen videoları tarihe göre süzme, izlenme ya da beğeniye göre sıralama, aylık grafik ve
  **CSV dışa aktarma**; takipçi geçmişi.
- **Hızlı sayfalar**, her cihazda.

## Kurulum ve kullanım

```bash
pip install git+https://github.com/social-content-fetcher/ttanon-viewer.git
```

```bash
ttanon-viewer link https://www.tiktok.com/@khaby.lame "#booktok"
ttanon-viewer open https://www.tiktok.com/@khaby.lame/video/7212345678901234567
```

```python
from ttanon_viewer import to_ttanon_url

to_ttanon_url("https://www.tiktok.com/@Khaby.Lame?lang=en")  # 'https://ttanon.com/@khaby.lame'
```

## TTAnon'un bir veri API'si var mı?

Hayır. TTAnon insanlar için bir web sitesidir; açık bir veri API'si sunmaz ve bu paket bir TikTok scraper'ı değildir.
Paketteki `TTAnonClient` veri çağrıları erişim anahtarı olmadan hiçbir istek göndermeden `AccessRestrictedError`
verir; hata, aynı içeriğin ttanon.com'daki adresini (`web_url`) taşır.

TikTok verisine ihtiyacınız varsa: [TikTok verisi nasıl alınır](docs/how-to-get-tiktok-data.md) (TikTok'un resmî
API'leri, kendi verinizi indirme, scraping'in neden nadiren buna değdiği).

## Rehberler (İngilizce)

- [TTAnon nedir?](docs/what-is-ttanon.md)
- [TikTok'u hesapsız izleme](docs/view-tiktok-without-account.md)
- [TikTok verisi nasıl alınır](docs/how-to-get-tiktok-data.md)
- [Neden doğrudan TTAnon](docs/why-use-ttanon-directly.md)
- [En iyi TikTok izleyici nasıl olmalı](docs/best-tiktok-viewer.md)
- [SSS](docs/faq.md)
- [Python istemci başvurusu](docs/api.md)

## Sık sorulanlar

**TikTok hesabı gerekir mi?** Hayır. Kayıt ve giriş yoktur.

**Gizli hesapları görebilir miyim?** Hayır. TTAnon yalnızca TikTok'un giriş yapmamış her ziyaretçiye gösterdiğini
gösterir.

**Profiline baktığımı kişi anlar mı?** TikTok'un profil görüntüleme geçmişi giriş yapmış TikTok hesaplarını listeler;
TTAnon'da hiçbir zaman giriş yapmış olmazsınız.

**TTAnon TikTok'a mı ait?** Hayır. TTAnon bağımsızdır; TikTok ya da ByteDance ile bağlantısı yoktur.

## Lisans

[MIT](LICENSE). TikTok, ByteDance Ltd.'nin ticari markasıdır. Bu proje TikTok ya da ByteDance ile bağlantılı değildir.
