# 🤖 Yapay Zeka Günlük İstihbarat Bülteni — 2026-11-08

> 📅 **Tarih:** 2026-11-08 | 🌐 **Dil:** Türkçe | ⚡ **Durum:** Otomatik Raporlandı

## ⚡ Yönetici Özeti (TL;DR)
* **MoE Mimarilerinde Seyreklik ve Hesaplama Verimliliği Zirveye Ulaşıyor:** Uzman sayılarının 384'e kadar tırmandığı yeni nesil açık kaynaklı MoE tasarımlarında (Kimi K2, DeepSeek-V4-Pro), artan seyreklik derecesi (örneğin 48 seyreklik) aynı doğrulama kaybında FLOP işlem yükünü 1,69 kat azaltarak çıkarım (inference) ve altyapı maliyetlerinde doğrudan belirleyici bir avantaj sağlıyor.
* **MXFP4 Kuantizasyonu ile Tek GPU'da 100B+ MoE Dağıtımı Mümkün:** gpt-oss-120b modelinin MXFP4 formatı sayesinde 117 milyar parametre ve katman başına 128 uzmanlık devasa mimariyi tek bir 80 GB GPU belleğine sığdırması, yüksek uzman paralelliği gerektiren ağ gecikmelerini ve donanım eşiğini düşürerek yerel dağıtımlarda yeni bir dönüm noktası oluşturuyor.
* **Açık Ağırlıklı Modellerde Hizalama ve Güvenlik İyileştirmesi:** Nous Research tarafından yayımlanan Arete-27B, Qwen3.8-27B modelindeki propaganda oranını %22 seviyesinden %0,9'a radikal biçimde düşürerek, kurumsal dağıtımlarda açık ağırlıklı (open-weights) modellerin güvenilirlik ve hizalama risklerini minimize ediyor.

---

## 🔬 Araştırma ve Çığır Açan Gelişmeler (Research & Breakthroughs)
### [Nous Research Releases Arete-27B that Cuts Qwen3.8-27B Propaganda From 22% to 0.9%](https://www.marktechpost.com/2026/11/07/nous-research-arete-27b-qwen3-8-27b-propaganda-fine-tune/)
**Öne Çıkanlar:**
  - Nous Research Releases Arete-27B that Cuts Qwen3.8-27B Propaganda From 22% to 0.9%: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
Nous Research released Arete-27B, an Apache 2.0 fine-tune of Qwen3.8-27B. On Nous’s 803-prompt eval, propaganda answers fell from 22% to 0.9% while Hermes Bench stayed flat at 65.60%. The post Nous Research Releases Arete-27B that Cuts Qwen3.8-27B Propaganda From 22% to 0.9% appeared first on MarkTechPost .

**Sektörel Etki & Anlamı:**
LLM Release alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [https://www.marktechpost.com/2026/11/07/nous-research-arete-27b-qwen3-8-27b-propaganda-fine-tune/](https://www.marktechpost.com/2026/11/07/nous-research-arete-27b-qwen3-8-27b-propaganda-fine-tune/)


---

## 🛠️ Araçlar, Modeller ve Açık Kaynak (Tooling, Frameworks & Releases)
### [Açık Kaynaklı MoE Modellerinde Yönlendirme Mimarilerinin Kapsamlı Karşılaştırması](https://www.marktechpost.com/2026/11/08/moe-model-routing-comparison/)
**Öne Çıkanlar:**
  - Uzman sayıları Mixtral modelindeki 8 adetten DeepSeek-V4-Pro ve Kimi K2 modellerindeki 384 adede kadar genişlemiş; top-k seçim parametresi ise Llama 4'teki 1'den DeepSeek-V3 ve Qwen3'teki 8'e kadar çeşitlilik göstermektedir.
  - Kimi K2 teknik raporuna göre, 48 seyreklik derecesi, aynı doğrulama kaybı seviyesinde 8 seyreklik derecesine kıyasla 1,69 kat daha az FLOP işlem yükü gerektirmektedir.
  - İncelenen 10 modelden 7'si her belirteç için her zaman devrede olan 1 paylaşımlı uzman kullanırken; Mixtral, gpt-oss ve Qwen3 paylaşımlı uzman yapısını içermemektedir.
  - DeepSeek-V4-Pro yönlendirme katmanlarında puanlama fonksiyonunu 'sqrtsoftplus'a taşımış, ilk 3 katmanda sabit özetleme (hash routing) yönlendirmesi uygulamış ve top-k değerini 8'den 6'ya düşürmüştür.
  - gpt-oss-120b modeli MXFP4 sayı formatı sayesinde 117 milyar toplam parametreye ve katman başına 128 uzmandan top-4 seçimine sahip olmasına rağmen tek bir 80 GB GPU belleğine sığabilmektedir.

**Teknik Derinlik & Mimari:**
Analiz edilen tüm açık MoE modelleri her belirtecin kendi uzmanlarını belirlediği belirteç-seçimli (token-choice) yönlendirme paradigmasını temel alır; ancak kapılama puanlama fonksiyonları ve yük dengeleme algoritmalarında ciddi mimari ayrışmalar bulunur. Klasik Softmax tabanlı kapılama (Mixtral, gpt-oss, Qwen3) yerini DeepSeek-V3, Kimi K2 ve GLM-4.5'te Sigmoid aktivasyonuna ve DeepSeek-V4'te sqrtsoftplus fonksiyonuna bırakmıştır. Yük dengeleme tarafında, geleneksel modeller loss fonksiyonuna harici yardımcı terimler (auxiliary loss) eklerken, DeepSeek ailesi ve türevleri (Kimi K2, GLM-4.5), karıştırma ağırlıklarını (mixing weights) bozmadan uzman seçimini yönlendiren yardımcı kayıpsız sapma optimizasyonunu ('noaux_tc') kullanmaktadır. Seyreklik mimarisinde ise Llama 4 Maverick, Switch Transformer yaklaşımını anımsatan ardışık yoğun/MoE katmanları ve top-1 yönlendirmesiyle 128 uzman arasından sadece 1'ini ve 1 paylaşımlı uzmanı etkinleştirerek belirteç başına 17 milyar aktif parametre çalıştırır. DeepSeek-V3 uzmanları 8 gruba ayırıp belirteç başına düğüm içi iletişimi en fazla 4 grupla sınırlandırırken, DeepSeek-V4 ilk 3 MoE katmanında dinamik yönlendirici yerine statik belirteç-uzman eşlemesi yapan 'hash routing' mekanizmasına geçmiştir.

**Sektörel Etki & Anlamı:**
Geliştiriciler ve altyapı mühendisleri için MoE modellerinin yönlendirme anatomisi, donanım kaynak planlaması ve çıkarım (inference) maliyeti üzerinde doğrudan belirleyicidir. Katman başına uzman sayısının 384'e çıkması bellek ayak izini ve uzman paralelliğindeki (expert parallelism) tümden-tüme (all-to-all) iletişim trafiğini artırırken, DeepSeek-V4'teki gibi top-k değerinin düşürülmesi belirteç başına hesaplama ve gecikmeyi hafifletir. Paylaşımlı uzmanların varlığı her belirteç için yoğun (dense) bir asgari hesaplama maliyeti yaratır. Ayrıca, Llama 4 ve gpt-oss'un dengeleme ve kapılama mekanizmalarını açık yapılandırmalarda gizlemesi şeffaflık eksikliği doğururken, gpt-oss'un MXFP4 formatıyla tek GPU'da çalışabilmesi düşük maliyetli yerel MoE dağıtımları için kritik bir dönüm noktasıdır.

📎 *Kaynak Bağlantısı:* [https://www.marktechpost.com/2026/11/08/moe-model-routing-comparison/](https://www.marktechpost.com/2026/11/08/moe-model-routing-comparison/)

---

### [MoE Routing Strategies Explained: Top-K, Expert-Choice, Sigmoid Gating and Dynamic Routing (2026 Guide)](https://www.marktechpost.com/2026/11/07/moe-routing-strategies-explained/)
**Öne Çıkanlar:**
  - MoE Routing Strategies Explained: Top-K, Expert-Choice, Sigmoid Gating and Dynamic Routing (2026 Guide): Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
MoE routing strategies decide which experts process each token. This guide explains 7 methods, from Mixtral's top-2 softmax to DeepSeek-V4's hash routing, with the models that use each one. The post MoE Routing Strategies Explained: Top-K, Expert-Choice, Sigmoid Gating and Dynamic Routing (2026 Guide) appeared first on MarkTechPost .

**Sektörel Etki & Anlamı:**
Research alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [https://www.marktechpost.com/2026/11/07/moe-routing-strategies-explained/](https://www.marktechpost.com/2026/11/07/moe-routing-strategies-explained/)


---

## 📚 Kaynak Rehberi ve Orijinal Bağlantılar
| # | Başlık | Kaynak | Doğrudan Link |
|---|---|---|---|
| 1 | Nous Research Releases Arete-27B that Cuts Qwen3.8-27B Propaganda From 22% to 0.9% | `www.marktechpost.com` | [İncele](https://www.marktechpost.com/2026/11/07/nous-research-arete-27b-qwen3-8-27b-propaganda-fine-tune/) |
| 2 | Açık Kaynaklı MoE Modellerinde Yönlendirme Mimarilerinin Kapsamlı Karşılaştırması | `www.marktechpost.com` | [İncele](https://www.marktechpost.com/2026/11/08/moe-model-routing-comparison/) |
| 3 | MoE Routing Strategies Explained: Top-K, Expert-Choice, Sigmoid Gating and Dynamic Routing (2026 Guide) | `www.marktechpost.com` | [İncele](https://www.marktechpost.com/2026/11/07/moe-routing-strategies-explained/) |

---
*Bu rapor LangGraph ve AI Multi-Agent StateGraph mimarisi ile her sabah otomatik olarak üretilmektedir.*
