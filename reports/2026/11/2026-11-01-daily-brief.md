# 🤖 Yapay Zeka Günlük İstihbarat Bülteni — 2026-11-01

> 📅 **Tarih:** 2026-11-01 | 🌐 **Dil:** Türkçe | ⚡ **Durum:** Otomatik Raporlandı

## ⚡ Yönetici Özeti (TL;DR)
* **Tek İleri Geçişle Deterministik Karar Mimarisi:** Nace AI'ın açık ağırlıklı 27B parametreli Drex Max v1 modeli, klasik ve yüksek maliyetli otoregresif metin üretimi yerine tek bir ileri geçişte (forward pass) 255 seçeneğe kadar olasılık dağılımı hesaplayarak ajan yönlendirme ve güvenlik denetimlerinde gecikme ile marjinal çıkarım maliyetlerini sıfıra indiriyor.
* **Uç Cihazlarda Yüksek Bağlamlı Yerel Altyapı:** Hibrit doğrusal dikkat (Gated DeltaNet) mimarisi ve Q4 kuantizasyonu sayesinde Drex Max v1, 262 bin tokenlik devasa bağlam penceresini MLX üzerinden 24 GB+ Apple Silicon donanımlarda tamamen çevrimdışı çalıştırarak kurumsal verileri buluta çıkarma zorunluluğunu ortadan kaldırıyor.
* **Açık Kaynak Kodlama Ajanlarında Modüler Dönem:** DeepSeek'in yönlendirici-işçi (router-worker) mimarisine dayanan `dsh-superagent` kodlama ajanını açık kaynak olarak yayımlaması, karmaşık yazılım geliştirme iş akışlarında özelleşmiş alt ajan ve açık ağırlıklı orkestrasyon araçlarının kullanımını standartlaştırıyor.

---

## 🔬 Araştırma ve Çığır Açan Gelişmeler (Research & Breakthroughs)
### [DeepSeek Open-Sources dsh-superagent, a Router-Worker Coding Agent](https://www.marktechpost.com/2026/11/01/deepseek-dsh-superagent-router-worker-coding-agent/)
**Öne Çıkanlar:**
  - DeepSeek Open-Sources dsh-superagent, a Router-Worker Coding Agent: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
DeepSeek released dsh-superagent, an MIT-licensed research prototype that turns GitHub and Feishu requests into parallel worker sessions. In DeepSeek’s own simulation, p95 task completion fell to 15.7 minutes from 29.5 minutes. The post DeepSeek Open-Sources dsh-superagent, a Router-Worker Coding Agent appeared first on MarkTechPost .

**Sektörel Etki & Anlamı:**
Tooling alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [https://www.marktechpost.com/2026/11/01/deepseek-dsh-superagent-router-worker-coding-agent/](https://www.marktechpost.com/2026/11/01/deepseek-dsh-superagent-router-worker-coding-agent/)


---

## 🛠️ Araçlar, Modeller ve Açık Kaynak (Tooling, Frameworks & Releases)
### [Nace AI, Apple Silicon Üzerinde Yerel Çalışabilen 27B Parametreli Karar Modeli Drex Max v1'i Açık Ağırlıklarla Erişime Açtı](https://www.marktechpost.com/2026/11/01/nace-ai-open-sources-drex-max-v1-local-inference/)
**Öne Çıkanlar:**
  - 27 milyar parametreli yoğun mimari, 48 adet Gated DeltaNet doğrusal dikkat ve 16 adet tam dikkat katmanını birleştirerek 262.144 tokenlik bağlam penceresi sunmaktadır.
  - Otokorelatif metin üretimi yerine tek bir ileri geçişte (forward pass) 255 seçeneğe kadar doğrudan olasılık dağılımı hesaplayan özel bir sınıflandırma başlığı kullanır.
  - Decision Index 0.4 kıyaslamasında 67,52 puan alarak Drex v2.0 (61,25) ve Jev 1.13.0 (57,96) modellerini geride bırakmıştır.
  - Affine Q4 kuantizasyonu ile 24 GB ve üzeri Apple Silicon donanımlarda MLX ve Kapitsa altyapısıyla tamamen çevrimdışı çalıştırılabilmektedir.

**Teknik Derinlik & Mimari:**
Drex Max v1, qwen3_5 omurgasını temel alan 64 katmanlı hibrit bir derin öğrenme mimarisine sahiptir. Modelin 48 katmanı soldan sağa çalışan Gated DeltaNet doğrusal dikkat mekanizmasını barındırırken, her dört katmanda bir konumlandırılan toplam 16 katman tam dikkat (full-attention) ve nedensel olmayan (non-causal) yapıdadır; bu sayede her token tüm dizilime çift yönlü erişebilir. Model token üretmek yerine, son gizli durumu (last hidden state) doğrudan 255 sınıflı bir okuma başlığına aktararak seçeneklerin olasılık dağılımlarını tek bir ileri geçişte hesaplar. Çok modlu girdiler için yerel görsel kule (vision tower) barındıran mimari, Apple Silicon üzerinde affine Q4 ve Q8_0 formatlarında çalıştırıldığında H100 bf16 referansına kıyasla 0,02 ila 0,0329 olasılık toleransı içinde kalarak karar stabilitesini korumaktadır.

**Sektörel Etki & Anlamı:**
Ajan yönlendirme (agent routing), güvenlik duvarı denetimleri (guardrail checks) ve çağrı sınıflandırma gibi kritik karar mekanizmaları genellikle yüksek maliyetli ve gecikmeli otokorelatif büyük dil modelleri üzerinden yürütülmektedir. Drex Max v1, üretim gerektirmeyen deterministik olasılık dağılımı mimarisi ve yerel donanım optimizasyonları sayesinde, mühendislerin hassas verileri buluta aktarmadan Apple Silicon ve yerel GPU'larda sıfır marjinal maliyetle, yüksek verimli çıkarım yapmalarına olanak tanımaktadır.

📎 *Kaynak Bağlantısı:* [https://www.marktechpost.com/2026/11/01/nace-ai-open-sources-drex-max-v1-local-inference/](https://www.marktechpost.com/2026/11/01/nace-ai-open-sources-drex-max-v1-local-inference/)


---

## 📚 Kaynak Rehberi ve Orijinal Bağlantılar
| # | Başlık | Kaynak | Doğrudan Link |
|---|---|---|---|
| 1 | DeepSeek Open-Sources dsh-superagent, a Router-Worker Coding Agent | `www.marktechpost.com` | [İncele](https://www.marktechpost.com/2026/11/01/deepseek-dsh-superagent-router-worker-coding-agent/) |
| 2 | Nace AI, Apple Silicon Üzerinde Yerel Çalışabilen 27B Parametreli Karar Modeli Drex Max v1'i Açık Ağırlıklarla Erişime Açtı | `www.marktechpost.com` | [İncele](https://www.marktechpost.com/2026/11/01/nace-ai-open-sources-drex-max-v1-local-inference/) |

---
*Bu rapor LangGraph ve AI Multi-Agent StateGraph mimarisi ile her sabah otomatik olarak üretilmektedir.*
