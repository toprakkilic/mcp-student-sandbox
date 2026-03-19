
# CENG302 Uygulama Çalışması Raporu

**Hazırlayan:** Abdullah Toprak Kılıç  
**Öğrenci No:** 23253071  
**GitHub Repo Adresi:** [toprakkilic/mcp-student-sandbox](https://github.com/toprakkilic/mcp-student-sandbox)

---

## 1. Çalışma Özeti ve Uygulama Adımları

Bu projede, VS Code üzerinde **GitHub Copilot Ajanları**  ve çeşitli **beceriler** kullanılarak modern yazılım geliştirme süreçleri simüle edilmiştir. 

### 2.1. spaghetti_logic.py
* **Kullanılan Ajan:** `@workspace`
* **İşlem:** Kodun karmaşıklığı analiz ettirilip "Clean Code" prensiplerine göre refactor edildi. Fonksiyonlar tek bir iş yapacak şekilde parçalandı.
* **Sonuç:** Kodun okunabilirliği ve sürdürülebilirliği artırıldı.

![Spaghetti Kod Analizi](https://github.com/toprakkilic/mcp-student-sandbox/raw/e2e44515f6feddf9dcb39317994a7048ed7580a4/rapor%EF%80%BFfotograflari/cleancode.png)
*Görsel 1: Copilot'un kod karmaşıklığını analiz edip refactoring önerdiği an.*

---

### 2.2. failing_calculator.py
* **Sorun:** `[10, 5, 0]` girişinde programın `ZeroDivisionError` vererek çökmesi.
* **İşlem:** Copilot hatanın kaynağını tespit etti. Sıfır değerlerini güvenli bir şekilde filtreleyen mantık eklendi.
* **GitHub Süreci:** Copilot tarafından profesyonel bir **Pull Request** taslağı oluşturuldu. Terminal üzerinden `git` komutlarıyla değişiklikler gönderildi.

![Hata Analizi](https://github.com/toprakkilic/mcp-student-sandbox/raw/e2e44515f6feddf9dcb39317994a7048ed7580a4/rapor%EF%80%BFfotograflari/2Hata%20analizi.png)
*Görsel 2: Hata analizi ve oluşturulan Pull Request taslağı.*

---

### 2.3. secret_leak.py
* **Analiz:** `@workspace` ajanı ile güvenlik taraması yapıldı.
* **Bulgu:** Dosya içinde açıkça yazılmış bir API anahtarı bulundu.
* **Aksiyon:** Bu güvenlik açığı için bir **GitHub Issue** oluşturuldu ve hassas verilerin `.env` dosyasında saklanması gerektiği raporlandı.

![Hata Analizi](https://github.com/toprakkilic/mcp-student-sandbox/raw/e2e44515f6feddf9dcb39317994a7048ed7580a4/rapor%EF%80%BFfotograflari/3secretkey.png)  
*Görsel 3: Tespit edilen API sızıntısı ve oluşturulan GitHub Issue kaydı.*

---

### 2.4. mystery_module.py
* **İşlem:** Karmaşık modül yapısı ajan tarafından incelenerek teknik bir `README.md` dosyası oluşturuldu.
* **Sonuç:** Kodun ne işe yaradığı, nasıl çalıştırılacağı ve parametreleri dökümante edildi.

---

## 3. Öz Değerlendirme

### A. Öğrendiklerim
* AI ajanlarının sadece kod tamamlamak için değil, projenin tüm yaşam döngüsünü yönetmek için kullanılabileceğini öğrendim.
* **Research Skill** kullanarak yapay zekanın geniş bir bilgi havuzundan nasıl faydalandığını deneyimledim.

### B. Havada Kalanlar
* **MCP** sunucularının yerel sistemdeki diğer araçlarla (veritabanı, özel CLI araçları) nasıl daha derin entegre edilebileceği konusu üzerinde daha fazla pratik yapmam gerekiyor.

### C. Diğer Söylemek İstediklerim

* **Profesyonel Dokümantasyon:** Copilot'un sunduğu taslakları incelediğimde, bir yazılımın yaşam döngüsünde **Commit mesajlarının** ve **Pull Request** açıklamalarının ne kadar detaylı ve açıklayıcı olması gerektiğini öğrendim.
* **Farkındalık:** Normalde commitlerimi tek bir satırda ve basit ifadelerle geçiştirirken; artık hatanın nedeni , çözüm yöntemi  ve test adımlarının belirtilmesinin  önemini fark ettim.
* **Sürekli Gelişim:** Bu çalışma, sadece kod yazmayı değil, yazılan kodun hikayesini ve güvenliğini (**PR/Issue/README**) profesyonel bir standartta sunmayı deneyimlememi sağladı.
* **Script Analizi:** Ödevle birlikte verilen `init_sandbox_gitskills.sh` dosyasını incelediğimde, GitHub CLI kontrol mekanizmasının yorum satırına  alınarak devre dışı bırakıldığını fark ettim.
* **Teknik Tespit:** Bu durumun, GitHub CLI yüklü olmayan sistemlerde script'in açıklayıcı bir hata vermeden yarıda kesilmesine yol açabileceğini fark ettim; çünkü kendi bilgisayarımda GitHub CLI yüklü değilken proje GitHub'a yüklenemiyor ve boş link veriyordu.
* **Aksiyon:** Script dosyasını incelerken, GitHub CLI kontrol mekanizmasının yorum satırına alınmış olduğunu fark ettim. Bu bölümün, kod yapısını analiz etmemiz ve bağımlılık yönetimini uygulama üzerinden kavramamız amacıyla bir öğrenme pratiği olarak bırakıldığını düşünerek ilgili satırları aktif hale getirdim. Bu sayede, otomasyon araçlarının arka planındaki sistem gereksinimlerini manuel olarak doğrulamanın ve hazırlık aşamasına hakim olmanın bir yazılımcı için ne kadar öğretici olduğunu bizzat deneyimleme fırsatı buldum.
