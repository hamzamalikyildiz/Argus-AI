# 🤖 Yapay Zeka Günlük İstihbarat Bülteni — 2026-10-22

> 📅 **Tarih:** 2026-10-22 | 🌐 **Dil:** Türkçe | ⚡ **Durum:** Otomatik Raporlandı

## ⚡ Yönetici Özeti (TL;DR)
- **[ArXiv] Direct Pass@k Thought Pruning**: Akıl yürütme modellerinde test zamanı hesaplama maliyetini düşürmek amacıyla çözüm kalitesi ve çeşitliliğini doğrudan dengeleyen pass@k optimizasyon yöntemi geliştirildi.
- **Google Cloud Agent Compute Engine**: Google Cloud, her yapay zeka ajanına özel donanım yalıtımlı MicroVM tahsis eden ve "zero credentials at rest" mimarisiyle çalışan yeni nesil ajan altyapısını duyurdu.
- **[ArXiv] METTA & EpiSEM-Bench**: Meta-öğrenmede lineer bellek ile hızlı adaptasyon sağlayan METTA mimarisi ve otonom ajanların eksik bilgi altındaki güvenlik açıklarını ölçen EpiSEM-Bench kıyaslaması yayınlandı.

---

## 🔬 Araştırma ve Çığır Açan Gelişmeler (Research & Breakthroughs)
### [[ArXiv] Direct Pass@k Optimization for Thought Pruning: Balancing Quality and Diversity in Test-Time Reasoning](http://arxiv.org/abs/2610.31667v1)
**Öne Çıkanlar:**
  - Akıl yürütme (reasoning) modellerinde test zamanı arama genişliğini budamak için pass@k metriğini doğrudan optimize eden yeni yöntem.
  - Sadece tekil kaliteye veya sadece çeşitliliğe odaklanan geleneksel budama stratejilerinin keşif/sömürü dengesizliğini giderir.
  - 8 açık ağırlıklı akıl yürütme modelinde en yüksek doğruluk ve hesaplama tasarrufu sağlandı.

**Teknik Derinlik & Mimari:**
Test-time scaling, akıl yürütme modellerinin çıkarım anında çok sayıda aday çözüm yolu üretmesi ve en az bir doğru sonuca ulaşması prensibine dayanır. Ancak tüm aday zincirleri sonuna kadar çalıştırmak aşırı hesaplama maliyeti doğurur. Önceki çalışmalar aday havuzunu erken aşamada (short prefix) budamak için ya tekil çözüm kalite puanına ya da kümeleme/çeşitlilik metriklerine dayanıyordu. Önerilen yöntem, çözüm havuzunu doğrudan pass@k metriğini maksimize edecek şekilde seçer; böylece kaliteli adayları ödüllendirirken fazlalık ve tekrarları (redundancy) cezalandırır. Bu sayede adaylar arasında kalite ve çeşitlilik doğal bir dengeye oturur.

**Sektörel Etki & Anlamı:**
Test-time compute (test zamanı hesaplama) ve akıl yürütme modellerinde çıkarım (inference) maliyetlerini ve gecikmeyi radikal biçimde düşürürken doğruluk oranını artırır.

📎 *Kaynak Bağlantısı:* [http://arxiv.org/abs/2610.31667v1](http://arxiv.org/abs/2610.31667v1)

---

### [[ArXiv] METTA: Memory-Enhanced Test-Time Adaptation for Meta-Reinforcement Learning](http://arxiv.org/abs/2610.31656v1)
**Öne Çıkanlar:**
  - Meta-pekiştirmeli öğrenmede (Meta-RL) test zamanı hızlı adaptasyon için çift ölçekli hafıza mimarisi.
  - Nedensel sinirsel hafıza (causal neural memory) ile doğrusal dizi karmaşıklığı ($O(N)$) sağlanır.
  - Meta-World ML10/ML45 ve PointMaze ortamlarında klasik transformer tabanlı modellere kıyasla üstün başarı oranı ve hız.

**Teknik Derinlik & Mimari:**
Klasik tekrarlayan (recurrent) ajanlar deneyimi gizli durumlara sıkıştırırken bilgi kaybeder; Transformer ajanları ise geçmiş yörüngeler üzerinde kuadratik bellek ve işlem maliyetine ($O(N^2)$) neden olur. METTA adaptasyon sürecini iki zamansal ölçeğe ayırır: Bölüm içi (within-episode) adaptasyonu lineer karmaşıklığa sahip nedensel sinirsel bellek çözerken, bölüm seviyesi (cross-episode) kompakt özetler uzun vadeli görev çıkarımını tüm geçmişe dikkat (attention) uygulamadan yürütür. Bu yapı sayesinde ajanlar daha önce hiç görmedikleri yeni ortamlara test zamanında etkin şekilde adapte olabilir.

**Sektörel Etki & Anlamı:**
Otonom ajanların ve robotik kontrol sistemlerinin daha önce hiç karşılaşmadıkları yeni görevlere ve fiziksel ortamlara sıfır gecikmeyle uyum sağlamasını kolaylaştırır.

📎 *Kaynak Bağlantısı:* [http://arxiv.org/abs/2610.31656v1](http://arxiv.org/abs/2610.31656v1)

---

### [[ArXiv] EpiSEM-Bench: Evaluating Safety and Evidence Recovery in LLM Agents under Missing Evidence](http://arxiv.org/abs/2610.31650v1)
**Öne Çıkanlar:**
  - Araç kullanan LLM ajanlarının eksik kanıt (missing evidence) altındaki güvenlik sınırlarını ölçen yeni kıyaslama (benchmark).
  - Çevresel veya araç yanıtlarında kritik güvenlik bilgileri atlandığında ajanların yasaklı eylemleri tetikleme riskini analiz eder.
  - 6 farklı alanda 300 eşleştirilmiş güvenli/güvensiz görev senaryosu ile 10 popüler dil modelini değerlendirir.

**Teknik Derinlik & Mimari:**
Araç kullanan ajanlar genellikle kullanıcı niyetinin zararsız olduğu ve aracın doğru bilgi döndüğü durumlarda bile, bir güvenlik gerçeği atlandığında tehlikeli eylemler gerçekleştirebilmektedir. EpiSEM-Bench, kritik olguları sistematik olarak baskılayarak modelin güvenli eylem durdurma eşiklerini ve eksik kanıtı aktif olarak arama/geri kazanma (evidence recovery) becerisini bağımsız bir denetçi aracıyla ölçmektedir. Araştırma, eksik bilgiye direncin aktif kanıt toplama becerisiyle her zaman örtüşmediğini ortaya koymaktadır.

**Sektörel Etki & Anlamı:**
Ajanik yapay zeka (Agentic AI) iş akışlarında araç çağırma (tool calling) ve otonom API yürütme güvenliği için kurumsal ölçekte kritik bir test standardı sunmaktadır.

📎 *Kaynak Bağlantısı:* [http://arxiv.org/abs/2610.31650v1](http://arxiv.org/abs/2610.31650v1)

---

## 🛠️ Araçlar, Modeller ve Açık Kaynak (Tooling, Frameworks & Releases)
### [Google Cloud Launches Agent Compute Engine: A MicroVM per AI Agent](https://www.marktechpost.com/2026/10/22/google-cloud-agent-compute-engine-microvm-ai-agents/)
**Öne Çıkanlar:**
  - Google Cloud, otonom yapay zeka ajanlarını barındırmak ve çalıştırmak için özel donanım yalıtımlı "Agent Compute Engine" platformunu duyurdu.
  - Her AI ajanına Google Titan silikonu ve Titanium IPU mimarisiyle desteklenen bağımsız bir MicroVM tahsis ediliyor.
  - "Zero credentials at rest" mimarisiyle ajan ortamında hiçbir kalıcı API anahtarı veya kimlik bilgisi tutulmuyor.
  - Kubernetes yerel (GKE) Agent Substrate açık kaynak çalışma zamanı (runtime) ile tam entegrasyon.

**Teknik Derinlik & Mimari:**
Geleneksel VM'lerin yavaş önyükleme süreleri ve standart konteynerlerin (Docker) çekirdek paylaşımı kaynaklı güvenlik açıklarına alternatif olarak Cloud Hypervisor tabanlı MicroVM mimarisi kullanılmıştır. Sistem prompt injection veya zararlı kod yürütme riskine karşı ajan ortamında statik kimlik bilgisi barındırmaz; tüm dış trafik yalıtılmış bir ağ geçidi üzerinden kısa ömürlü ve kapsamlı kimliklerle yönlendirilir. Ayrıca ajanların bekleme sürelerinde bellek paylaşımı (copy-on-write) ve anlık görüntü dondurma/geri yükleme (snapshot checkpoint/restore) ile işlem maliyetleri minimize edilir.

**Sektörel Etki & Anlamı:**
Kurumsal ölçekte otonom ajanların üretim ortamlarında güvenli, yalıtılmış ve düşük maliyetli biçimde konuşlandırılması için sektördeki ilk donanım destekli MicroVM standardını belirlemektedir.

📎 *Kaynak Bağlantısı:* [https://www.marktechpost.com/2026/10/22/google-cloud-agent-compute-engine-microvm-ai-agents/](https://www.marktechpost.com/2026/10/22/google-cloud-agent-compute-engine-microvm-ai-agents/)

---

## 📚 Kaynak Rehberi ve Orijinal Bağlantılar
| # | Başlık | Kaynak | Doğrudan Link |
|---|---|---|---|
| 1 | [ArXiv] Direct Pass@k Optimization for Thought Pruning: Balancing Quality and Diversity in Test-Time Reasoning | `arxiv.org` | [İncele](http://arxiv.org/abs/2610.31667v1) |
| 2 | [ArXiv] METTA: Memory-Enhanced Test-Time Adaptation for Meta-Reinforcement Learning | `arxiv.org` | [İncele](http://arxiv.org/abs/2610.31656v1) |
| 3 | [ArXiv] EpiSEM-Bench: Evaluating Safety and Evidence Recovery in LLM Agents under Missing Evidence | `arxiv.org` | [İncele](http://arxiv.org/abs/2610.31650v1) |
| 4 | Google Cloud Launches Agent Compute Engine: A MicroVM per AI Agent | `marktechpost.com` | [İncele](https://www.marktechpost.com/2026/10/22/google-cloud-agent-compute-engine-microvm-ai-agents/) |

---
*Bu rapor LangGraph ve AI Multi-Agent StateGraph mimarisi ile her sabah otomatik olarak üretilmektedir.*
