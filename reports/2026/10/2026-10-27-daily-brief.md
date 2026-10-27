# 🤖 Yapay Zeka Günlük İstihbarat Bülteni — 2026-10-27

> 📅 **Tarih:** 2026-10-27 | 🌐 **Dil:** Türkçe | ⚡ **Durum:** Otomatik Raporlandı

## ⚡ Yönetici Özeti (TL;DR)
* **Ajan İş Yüklerinde Çıkarım Maliyeti Devrimi:** OpenAI, GPT-6.1 Sol API maliyetlerini yarıya indiren **GPT-6.1 Terra**'yı duyurdu. Yüksek token tüketimine sahip otonom ajan sistemleri geliştiren mühendisler ve liderler için bu fiyat indirimi, üretim ölçeğindeki bütçe ve bilgi işlem (compute) engellerini doğrudan azaltıyor.
* **LLM Sunum Altyapılarında Kritik Güvenlik Uyarısı:** GLM-5.3 Workers AI üzerinde belgelenen **istekler arası (cross-request) KV cache sızıntısı**, paylaşımlı ve çok kiracılı (multi-tenant) çıkarım altyapılarında bellek izolasyonunun ne kadar kritik olduğunu gösteriyor; mühendislik ekiplerinin donanım düzeyinde önbellek güvenliğini acilen denetlemesi gerekiyor.
* **Açık Ağırlıklı Karar Mekanizmalarında Ölçek Büyümesi:** vLLM Semantic Router ekibinin 27B parametreli açık çok modlu karar modeli **d3-ultra**'yı yayınlaması, özel API bağımlılığını azaltmak isteyen ekipler için yerel orkestrasyon ve iş yükü yönlendirmede açık ağırlıklı alternatifleri güçlü bir konuma taşıyor.

---

## 🔬 Araştırma ve Çığır Açan Gelişmeler (Research & Breakthroughs)
### [[ArXiv] Retriever-Free Retrieval: Navigating Documents with Decision Models](http://arxiv.org/abs/2610.35868v1)
**Öne Çıkanlar:**
  - [ArXiv] Retriever-Free Retrieval: Navigating Documents with Decision Models: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
While language models have become dramatically more capable, retrieval still largely relies on lexical matching or similarity in fixed embedding spaces. This creates a capability asymmetry: what the retriever fails to find, even the strongest generator cannot recover. We propose DecisionRAG, which brings the capabilities of pretrained language models to retrieval using decision models that jointly evaluate candidate branches in a single forward pass, without generating any tokens, and show that judging candidates in a shared context makes their relevance estimates comparable. Like a person browsing a library, DecisionRAG navigates the corpus's inherent structure from broad topics down to individual passages, deciding at each level which branches are worth exploring. Without task-specific training or a first-stage retriever, DecisionRAG outperforms dense retrieval with an 8B reranker by 13.8 R@1 points on MultiDoc2Dial and 17.4 Hit@1 points on Natural Questions. Across four benchmarks, including a corpus of 2.68 million Wikipedia paragraphs, retrieval takes just 0.7-1.8 seconds per query.

**Sektörel Etki & Anlamı:**
Research alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [http://arxiv.org/abs/2610.35868v1](http://arxiv.org/abs/2610.35868v1)

---

### [[ArXiv] Learning Force-Reactive Humanoid Loco-Manipulation](http://arxiv.org/abs/2610.35862v1)
**Öne Çıkanlar:**
  - [ArXiv] Learning Force-Reactive Humanoid Loco-Manipulation: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
Many everyday tasks require controlling contact force as well as motion. On a humanoid, this force must often be coordinated across both hands and the whole body, and cannot be specified by kinematic trajectories alone. Therefore, we present FLORE, a framework for learning force-reactive humanoid loco-manipulation. We collect robot-free demonstrations using two force-sensing UMI-style handheld grippers for hand motion and contact wrenches, and wearable trackers for body motion. A force-reactive diffusion policy takes vision, proprioception, and measured wrenches as input, then predicts actions and per-hand force commands. A hybrid compliance whole-body controller with force tracking executes these commands while maintaining balance: an integral of the force error measured by real force/torque (F/T) sensors lets each hand track force accurately along the commanded direction and remain compliant along the others. In simulation, the controller tracks per-hand force commands of varied magnitude and direction, with little loss in whole-body motion accuracy. Across three contact-rich tasks on the robot, the force-reactive policy succeeds in 80% of rollouts, compared with 26.7% for a position-only policy trained on the same demonstrations and executed by the same controller. For more details, please visit our website: https://louis-leee.github.io/FLoRe/.

**Sektörel Etki & Anlamı:**
Research alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [http://arxiv.org/abs/2610.35862v1](http://arxiv.org/abs/2610.35862v1)

---

### [[ArXiv] Patient-specific rubric-based evaluation of large language models across longitudinal cancer care](http://arxiv.org/abs/2610.35847v1)
**Öne Çıkanlar:**
  - [ArXiv] Patient-specific rubric-based evaluation of large language models across longitudinal cancer care: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
Large language models (LLMs) show promise in specialty medicine, yet existing evaluations largely focus on isolated clinical encounters rather than tracking how clinical responsibilities evolve across a longitudinal care pathway. Here we introduce NPC-RubricBench, a phase-aware benchmark for evaluating multistage clinical reasoning across the cancer care continuum, using nasopharyngeal carcinoma as a defined disease context. Curated from longitudinal records of 405 patients across two cancer centers, the benchmark comprises 941 patient-phase units across six sequential care phases and 17,688 patient-specific atomic criteria spanning five evaluation dimensions, with each assessment strictly restricted to decision-time clinical evidence. Evaluating 30 general-purpose and medical LLMs revealed that strong diagnostic performance does not carry over to downstream care. We evaluated 30 general-purpose and medical LLMs, showing that high diagnostic performance did not translate into improved downstream care. Instead, the dominant failure modes reversed across phases. Explicit decision errors dominated anatomical staging at 48.2%, whereas decision omissions dominated initial work-up and post-treatment follow-up at 33.4% and 30.4%, respectively. In the evaluated model set, medically adapted models showed higher omission rates than general-purpose models. Moreover, varying query granularity exposes a critical specification trade-off: broad open-ended requests degrade Decision Quality a

**Sektörel Etki & Anlamı:**
Research alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [http://arxiv.org/abs/2610.35847v1](http://arxiv.org/abs/2610.35847v1)


---

## 🛠️ Araçlar, Modeller ve Açık Kaynak (Tooling, Frameworks & Releases)
### [OpenAI Launches GPT-6.1 Terra, Halving GPT-6.1 Sol’s API Price for Agent Work](https://www.marktechpost.com/2026/10/26/openai-gpt-6-1-terra/)
**Öne Çıkanlar:**
  - OpenAI Launches GPT-6.1 Terra, Halving GPT-6.1 Sol’s API Price for Agent Work: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
OpenAI released GPT-6.1 Terra, a fast computer-use and vision model priced at $1/$5 per million tokens. It matches GPT-6 Astra’s medium-effort Agents’ Last Exam score at $0.29 per task versus $4.82. The post OpenAI Launches GPT-6.1 Terra, Halving GPT-6.1 Sol’s API Price for Agent Work appeared first on MarkTechPost .

**Sektörel Etki & Anlamı:**
LLM Release alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [https://www.marktechpost.com/2026/10/26/openai-gpt-6-1-terra/](https://www.marktechpost.com/2026/10/26/openai-gpt-6-1-terra/)

---

### [Cross-request KV cache exposure in the GLM-5.3 Workers AI model (155 responses)](https://blog.cloudflare.com/kv-cache-exposure-remediation/)
**Öne Çıkanlar:**
  - Cross-request KV cache exposure in the GLM-5.3 Workers AI model (155 responses): Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
Article URL: https://blog.cloudflare.com/kv-cache-exposure-remediation/ Comments URL: https://news.ycombinator.com/item?id=50252159 Points: 135 # Comments: 43

**Sektörel Etki & Anlamı:**
Tooling alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [https://blog.cloudflare.com/kv-cache-exposure-remediation/](https://blog.cloudflare.com/kv-cache-exposure-remediation/)

---

### [vLLM Semantic Router Releases d3-ultra: A 27B Open Multimodal Decision Model](https://www.marktechpost.com/2026/10/26/vllm-semantic-router-d3-ultra-27b-multimodal-decision-model/)
**Öne Çıkanlar:**
  - vLLM Semantic Router Releases d3-ultra: A 27B Open Multimodal Decision Model: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
vLLM Semantic Router released d3-ultra, a 27B open-weight multimodal decision model. It reads text, images and video once, then returns probabilities for every answer, scoring 87.2 on the team’s SR-Text test. The post vLLM Semantic Router Releases d3-ultra: A 27B Open Multimodal Decision Model appeared first on MarkTechPost .

**Sektörel Etki & Anlamı:**
LLM Release alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [https://www.marktechpost.com/2026/10/26/vllm-semantic-router-d3-ultra-27b-multimodal-decision-model/](https://www.marktechpost.com/2026/10/26/vllm-semantic-router-d3-ultra-27b-multimodal-decision-model/)

---

### [Baidu Open-Sources Unlimited OCR 2 for Hundred-Page Document Parsing](https://www.marktechpost.com/2026/10/26/baidu-unlimited-ocr-2-open-source-long-document-ocr/)
**Öne Çıkanlar:**
  - Baidu Open-Sources Unlimited OCR 2 for Hundred-Page Document Parsing: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
Baidu has released Unlimited OCR 2, an MIT-licensed 3B OCR model that parses hundred-page documents in one request. Its SR-SWA attention keeps per-step decoding cost nearly flat, scoring 77.1 on MarathonDocBench The post Baidu Open-Sources Unlimited OCR 2 for Hundred-Page Document Parsing appeared first on MarkTechPost .

**Sektörel Etki & Anlamı:**
LLM Release alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [https://www.marktechpost.com/2026/10/26/baidu-unlimited-ocr-2-open-source-long-document-ocr/](https://www.marktechpost.com/2026/10/26/baidu-unlimited-ocr-2-open-source-long-document-ocr/)


---

## 📚 Kaynak Rehberi ve Orijinal Bağlantılar
| # | Başlık | Kaynak | Doğrudan Link |
|---|---|---|---|
| 1 | OpenAI Launches GPT-6.1 Terra, Halving GPT-6.1 Sol’s API Price for Agent Work | `www.marktechpost.com` | [İncele](https://www.marktechpost.com/2026/10/26/openai-gpt-6-1-terra/) |
| 2 | [ArXiv] Retriever-Free Retrieval: Navigating Documents with Decision Models | `arxiv.org` | [İncele](http://arxiv.org/abs/2610.35868v1) |
| 3 | Cross-request KV cache exposure in the GLM-5.3 Workers AI model (155 responses) | `blog.cloudflare.com` | [İncele](https://blog.cloudflare.com/kv-cache-exposure-remediation/) |
| 4 | vLLM Semantic Router Releases d3-ultra: A 27B Open Multimodal Decision Model | `www.marktechpost.com` | [İncele](https://www.marktechpost.com/2026/10/26/vllm-semantic-router-d3-ultra-27b-multimodal-decision-model/) |
| 5 | Baidu Open-Sources Unlimited OCR 2 for Hundred-Page Document Parsing | `www.marktechpost.com` | [İncele](https://www.marktechpost.com/2026/10/26/baidu-unlimited-ocr-2-open-source-long-document-ocr/) |
| 6 | [ArXiv] Learning Force-Reactive Humanoid Loco-Manipulation | `arxiv.org` | [İncele](http://arxiv.org/abs/2610.35862v1) |
| 7 | [ArXiv] Patient-specific rubric-based evaluation of large language models across longitudinal cancer care | `arxiv.org` | [İncele](http://arxiv.org/abs/2610.35847v1) |

---
*Bu rapor LangGraph ve AI Multi-Agent StateGraph mimarisi ile her sabah otomatik olarak üretilmektedir.*
