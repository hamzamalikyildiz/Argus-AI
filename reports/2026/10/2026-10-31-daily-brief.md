# 🤖 Yapay Zeka Günlük İstihbarat Bülteni — 2026-10-31

> 📅 **Tarih:** 2026-10-31 | 🌐 **Dil:** Türkçe | ⚡ **Durum:** Otomatik Raporlandı

## ⚡ Yönetici Özeti (TL;DR)
- **[ArXiv] Rethinking Neural Thickets Without Weight Perturbations**: [ArXiv] Rethinking Neural Thickets Without Weight Perturbations: Gelişme detayları inceleniyor.
- **Ayrık Difüzyon Modelleri İçin Deterministik ODE Tabanlı Örnekleme: Üstel Artık Akışları**: Sürekli difüzyon modellerindeki Olasılık Akışı ODE'sinin (Probability Flow ODE) ayrık difüzyon modelleri için karşılığı olan Üstel Artık Akışları (Exponential Residual Flows - ERF) matematiksel olarak türetilmiştir.
- **Vercel Labs Open-Sources agent-desktop for Agent Computer Use**: Vercel Labs Open-Sources agent-desktop for Agent Computer Use: Gelişme detayları inceleniyor.

---

## 🔬 Araştırma ve Çığır Açan Gelişmeler (Research & Breakthroughs)
### [[ArXiv] Rethinking Neural Thickets Without Weight Perturbations](http://arxiv.org/abs/2610.40649v1)
**Öne Çıkanlar:**
  - [ArXiv] Rethinking Neural Thickets Without Weight Perturbations: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
The Neural Thickets hypothesis posits that pretrained language models lie in dense neighborhoods of task-specific experts in weight space, which random Gaussian perturbations can uncover. We reproduce the reported gains, but show that they do not require this geometric explanation. Perturbing a single decoder block already recovers much of the improvement, while keeping the model entirely frozen and adding a random bias to its output logits matches or exceeds full-weight perturbations on most reasoning tasks. This suggests an alternative explanation based on output diversity, validation-based selection, and voting. We formalize this view as Perturb-Select-Vote (PSV), a general procedure that generates perturbed predictors, selects high-performing members on a small validation set, and aggregates their predictions. This interpretation connects Neural Thickets to established inference-time methods, including sampling, self-consistency, and verifier-guided selection. A first-order analysis further shows that small weight perturbations act primarily through their induced logit shifts. We extend this analysis to vision, where logit PSV substantially improves performance under domain shift, including on Earth observation, while full-weight perturbations provide little additional benefit. Together, these results suggest that the gains attributed to nearby weight-space experts can instead be obtained through output diversity, selection, and voting. Logit PSV realizes these benefits w

**Sektörel Etki & Anlamı:**
Research alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [http://arxiv.org/abs/2610.40649v1](http://arxiv.org/abs/2610.40649v1)

---

### [Ayrık Difüzyon Modelleri İçin Deterministik ODE Tabanlı Örnekleme: Üstel Artık Akışları](http://arxiv.org/abs/2610.40618v1)
**Öne Çıkanlar:**
  - Sürekli difüzyon modellerindeki Olasılık Akışı ODE'sinin (Probability Flow ODE) ayrık difüzyon modelleri için karşılığı olan Üstel Artık Akışları (Exponential Residual Flows - ERF) matematiksel olarak türetilmiştir.
  - Ayrık durum uzayı, her belirteç ve konum için sürekli bir artık değişkenle desteklenmiş; artık değişkenin sıfıra ulaştığı anlarda durum geçişi tetiklenerek marjinal dağılımın tam korunumu kanıtlanmıştır.
  - Parçalı tanımlı deterministik ODE yapısı, ayrık difüzyon süreçlerinde ilk kez doğrudan tutarlılık damıtması (consistency distillation) uygulanabilmesini mümkün kılmıştır.
  - Maskelenmiş (masked) ve tekdüze (uniform) difüzyon şemalarına uyarlanan örnekleyici, kod ve metin üretiminde önceki stokastik ayrık difüzyon yöntemlerine kıyasla daha yüksek örnekleme verimliliği ve başarım sunmaktadır.

**Teknik Derinlik & Mimari:**
Sürekli difüzyon modellerinde marjinal dağılımlar deterministik bir ODE ile tam olarak modellenip hızlı örnekleme sağlanabilirken, ayrık difüzyon şimdiye kadar stokastik Markov sıçrama süreçlerine bağımlı kalmıştır. Bu çalışma, ayrık durumları her token ve pozisyon için sürekli bir artık değişkenle genişleten Üstel Artık Akışları (ERF) çerçevesini tanıtmaktadır. Bu artıklar, mevcut ayrık durum ile ileri/geri geçiş oranı matrislerine (rate matrices) bağlı vektör alanları üzerinden parçalı tanımlı deterministik ODE'ler uyarınca evrilir. Bir artık değişken sıfıra temas ettiğinde ayrık durum deterministik olarak güncellenir. Makalede, bu dinamiklerin orijinal difüzyon sürecinin marjinal dağılımlarını kesin olarak koruduğu ispatlanmıştır. Bu deterministik yörüngeler, ayrık difüzyonda tutarlılık damıtmasının (consistency distillation) önünü açarak çok az sayıda fonksiyon değerlendirmesiyle (NFE) yüksek kaliteli örneklemeyi pratik hale getirmektedir.

**Sektörel Etki & Anlamı:**
Ayrık difüzyon modellerinin metin ve kaynak kod gibi alanlarda yaygınlaşmasının önündeki en büyük engel, yüksek çıkarım adımı gereksinimi ve deterministik hızlandırıcı ODE çözücülerinin eksikliğiydi. ERF, sürekli difüzyonun sunduğu analitik hızlandırma ve damıtma avantajlarını ayrık dizilim uzayına taşıyarak, otoregresif olmayan (non-autoregressive) dil ve kod üretim mimarilerinde çıkarım gecikmesini kökten azaltabilecek teorik ve pratik bir zemin sunmaktadır.

📎 *Kaynak Bağlantısı:* [http://arxiv.org/abs/2610.40618v1](http://arxiv.org/abs/2610.40618v1)

---

### [[ArXiv] Read, Allocate, Route: Role-Coupled Tokenization for Pixel-Space Generative Transformers](http://arxiv.org/abs/2610.40647v1)
**Öne Çıkanlar:**
  - [ArXiv] Read, Allocate, Route: Role-Coupled Tokenization for Pixel-Space Generative Transformers: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
Pixel-space generative Transformers typically use one token per image patch, so capturing finer detail requires more tokens and makes global attention increasingly expensive. We observe that finer detail does not necessarily require more global communication: low-frequency structure benefits from global exchange, while high-frequency detail can be modeled locally. Based on this insight, we introduce SpecSlot, a pixel-space rectified-flow Transformer that decouples output detail from the length of the global attention sequence. SpecSlot expands each spatial anchor into multiple slots, each assigned a disjoint band of DCT coefficients; this separates anchor density from spectral subdivision. Only the lowest-frequency slot from each anchor participates in global attention, while all slots interact locally. This allows the model to increase spectral detail without enlarging the global sequence. A spatial head further adds a local correction to the spectral prediction, while the generative state, target, and loss remain in pixel space. On ImageNet-256, SpecSlot achieves a comparable final FID to a FLOPs-matched JiT control while converging faster. On ImageNet-512, it improves FID by 2.84 over the control with 3.9% fewer FLOPs, and comes within only 0.69 FID of JiT-B/16 at 38.2% lower cost. On text-to-image generation, SpecSlot surpasses JiT-B/8 on DPG-Bench by 1.06 at 40.6% lower forward cost.

**Sektörel Etki & Anlamı:**
Research alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [http://arxiv.org/abs/2610.40647v1](http://arxiv.org/abs/2610.40647v1)

---

### [[ArXiv] TextSeal2: Distortion-Free LLM Watermarking with Copula Mixing and Memoryless Races](http://arxiv.org/abs/2610.40613v1)
**Öne Çıkanlar:**
  - [ArXiv] TextSeal2: Distortion-Free LLM Watermarking with Copula Mixing and Memoryless Races: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
We present TextSeal2, a distortion-free watermark for large language models that keeps its signal under speculative decoding: tokens that replace rejected drafts remain watermarked with the same keys, and the acceptance rate is unchanged. It also preserves output diversity and adds no measurable inference latency. Its predecessor, TextSeal, restores diversity in the Gumbel-max scheme by routing each token to one of two keys via a coin flip. This is suboptimal because the detector averages the scores from both keys without knowing which key was used. TextSeal2 instead merges two or more keys into a single virtual key and couples it to fresh noise through AutoMark's Gaussian copula. Any number of keys, including publicly shared keys, can be merged this way without diluting detection. Under speculative decoding, TextSeal2 verifies keyed drafts with one more exponential race, run on the leftovers of the draft races. By memorylessness, this race reproduces block verification, so the output follows the target model exactly. We evaluate TextSeal2 on three LLMs. At equal output token diversity, TextSeal2 detects 8 to 22 percentage points more 100-token answers than TextSeal at a false-positive rate of $10^{-3}$, and is comparable to textGrain while requiring no post-logits optimization. Under speculative decoding, it detects 18 and 22 percentage points more 200-token answers than TextSeal and textGrain, respectively, at the same acceptance rate.

**Sektörel Etki & Anlamı:**
Research alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [http://arxiv.org/abs/2610.40613v1](http://arxiv.org/abs/2610.40613v1)

---

### [[ArXiv] world2vec: Mechanistic world models through latent dynamics learning](http://arxiv.org/abs/2610.40637v1)
**Öne Çıkanlar:**
  - [ArXiv] world2vec: Mechanistic world models through latent dynamics learning: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
World models can achieve strong control performance without faithfully capturing the dynamics of their environment, limiting their potential for mechanistic interpretability and scientific discovery. Here, we introduce world2vec to learn mechanistic world models without reward information directly from observations and actions. World2vec learns latent dynamics that faithfully reproduce the true system over long prediction horizons, with at least one order of magnitude fewer parameters than DreamerV3, TD-MPC2 and LeWM. This enables state of the art performance in controlling continuous environments from pixels and accurate system identification across a benchmark of 71 attractors, demonstrating how world models are amenable to scientific discovery.

**Sektörel Etki & Anlamı:**
Research alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [http://arxiv.org/abs/2610.40637v1](http://arxiv.org/abs/2610.40637v1)

---

### [[ArXiv] Elucidating the Design Space of LM Data Attribution](http://arxiv.org/abs/2610.40655v1)
**Öne Çıkanlar:**
  - [ArXiv] Elucidating the Design Space of LM Data Attribution: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
Data attribution methods for Language Models (LMs) are typically evaluated using downstream tasks like fact retrieval. However, existing evaluations vary multiple dataset properties simultaneously, making it impossible to isolate exactly why an attribution algorithm fails. To diagnose these failures, we explore the design space of LLM data attribution, with a primary focus on evaluation. We introduce the Controlled Attribution Benchmark (CATT) for fact tracing, in which we fine-tune LLMs on entirely fictitious knowledge, providing unambiguous ground truth for attribution. This synthetic setup allows us to systematically alter one dataset configuration at a time, such as document redundancy and lexical distractors. With this configurable evaluation, we demonstrate that redundancy and distractors consistently degrade attribution performance. Rather than proposing a new estimator, we examine two design choices that are underexplored: the loss used to compute gradients and how per-token attribution scores are aggregated into a document score. We find that the true causal evidence within a training document is highly localized, but standard methods dilute this evidence into noise by averaging attribution scores across the entire document. We find that replacing standard cross-entropy loss gradients with the negative log-odds gradients surfaces the critical tokens from other uninformative ones. We can then aggregate only the top token scores to improve ground truth recall by 35 to 

**Sektörel Etki & Anlamı:**
Research alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [http://arxiv.org/abs/2610.40655v1](http://arxiv.org/abs/2610.40655v1)


---

## 🛠️ Araçlar, Modeller ve Açık Kaynak (Tooling, Frameworks & Releases)
### [Vercel Labs Open-Sources agent-desktop for Agent Computer Use](https://www.marktechpost.com/2026/10/31/vercel-labs-agent-desktop-computer-use/)
**Öne Çıkanlar:**
  - Vercel Labs Open-Sources agent-desktop for Agent Computer Use: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
Vercel Labs released agent-desktop, an Apache-2.0 Rust CLI that gives any AI agent computer use on macOS, Windows and Linux by reading OS accessibility trees and acting on stable refs instead of pixels. The post Vercel Labs Open-Sources agent-desktop for Agent Computer Use appeared first on MarkTechPost .

**Sektörel Etki & Anlamı:**
Tooling alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [https://www.marktechpost.com/2026/10/31/vercel-labs-agent-desktop-computer-use/](https://www.marktechpost.com/2026/10/31/vercel-labs-agent-desktop-computer-use/)

---

### [Meet TokenEconomizer: Microsoft’s Plugin That Cuts Coding Agent Costs by Up to 30.9%](https://www.marktechpost.com/2026/10/30/microsoft-tokeneconomizer-coding-agent-cost-control/)
**Öne Çıkanlar:**
  - Meet TokenEconomizer: Microsoft’s Plugin That Cuts Coding Agent Costs by Up to 30.9%: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
Microsoft Research and UC Berkeley released TokenEconomizer, an open-source plugin that learns from past sessions to cut coding agent token costs by 18.4% to 30.9% on SWE-Bench, with no change to the agent. The post Meet TokenEconomizer: Microsoft’s Plugin That Cuts Coding Agent Costs by Up to 30.9% appeared first on MarkTechPost .

**Sektörel Etki & Anlamı:**
Tooling alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [https://www.marktechpost.com/2026/10/30/microsoft-tokeneconomizer-coding-agent-cost-control/](https://www.marktechpost.com/2026/10/30/microsoft-tokeneconomizer-coding-agent-cost-control/)


---

## 📚 Kaynak Rehberi ve Orijinal Bağlantılar
| # | Başlık | Kaynak | Doğrudan Link |
|---|---|---|---|
| 1 | [ArXiv] Rethinking Neural Thickets Without Weight Perturbations | `arxiv.org` | [İncele](http://arxiv.org/abs/2610.40649v1) |
| 2 | Ayrık Difüzyon Modelleri İçin Deterministik ODE Tabanlı Örnekleme: Üstel Artık Akışları | `arxiv.org` | [İncele](http://arxiv.org/abs/2610.40618v1) |
| 3 | Vercel Labs Open-Sources agent-desktop for Agent Computer Use | `www.marktechpost.com` | [İncele](https://www.marktechpost.com/2026/10/31/vercel-labs-agent-desktop-computer-use/) |
| 4 | Meet TokenEconomizer: Microsoft’s Plugin That Cuts Coding Agent Costs by Up to 30.9% | `www.marktechpost.com` | [İncele](https://www.marktechpost.com/2026/10/30/microsoft-tokeneconomizer-coding-agent-cost-control/) |
| 5 | [ArXiv] Read, Allocate, Route: Role-Coupled Tokenization for Pixel-Space Generative Transformers | `arxiv.org` | [İncele](http://arxiv.org/abs/2610.40647v1) |
| 6 | [ArXiv] TextSeal2: Distortion-Free LLM Watermarking with Copula Mixing and Memoryless Races | `arxiv.org` | [İncele](http://arxiv.org/abs/2610.40613v1) |
| 7 | [ArXiv] world2vec: Mechanistic world models through latent dynamics learning | `arxiv.org` | [İncele](http://arxiv.org/abs/2610.40637v1) |
| 8 | [ArXiv] Elucidating the Design Space of LM Data Attribution | `arxiv.org` | [İncele](http://arxiv.org/abs/2610.40655v1) |

---
*Bu rapor LangGraph ve AI Multi-Agent StateGraph mimarisi ile her sabah otomatik olarak üretilmektedir.*
