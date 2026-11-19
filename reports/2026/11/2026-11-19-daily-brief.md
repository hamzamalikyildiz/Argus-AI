# 🤖 Yapay Zeka Günlük İstihbarat Bülteni — 2026-11-19

> 📅 **Tarih:** 2026-11-19 | 🌐 **Dil:** Türkçe | ⚡ **Durum:** Otomatik Raporlandı

## ⚡ Yönetici Özeti (TL;DR)
- **Google DeepMind Releases Gemini 4 Neon: 1M Context, #1 on AA Coding Agent Index**: Google DeepMind Releases Gemini 4 Neon: 1M Context, #1 on AA Coding Agent Index: Gelişme detayları inceleniyor.
- **New LoRA Adapter Lifts Qwen3.8 Coding Success From 39% to 65%**: New LoRA Adapter Lifts Qwen3.8 Coding Success From 39% to 65%: Gelişme detayları inceleniyor.
- **[ArXiv] General progress substitutes for specific training data in language models**: [ArXiv] General progress substitutes for specific training data in language models: Gelişme detayları inceleniyor.

---

## 🔬 Araştırma ve Çığır Açan Gelişmeler (Research & Breakthroughs)
### [[ArXiv] General progress substitutes for specific training data in language models](http://arxiv.org/abs/2611.24844v1)
**Öne Çıkanlar:**
  - [ArXiv] General progress substitutes for specific training data in language models: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
Language models acquire their capabilities from training data, and developers withhold data during training to keep models from learning capabilities that could be misused. How long this delays a capability, and how much data is needed to acquire it later, is unknown. Here we show that the general progress a model makes on the rest of its training data substitutes for the data that was withheld. We withheld the training signal for individual skills in models of chess, Othello, molecular strings, bracket languages and web text. The delay of a withheld skill in larger models was predicted from smaller ones. A chess model never explicitly trained to respond to check ranked the legal responses almost as well as a model that was. When models were then trained on the withheld data, they acquired the skill with a small fraction of the data needed from initialization, and this fraction decreased as the models progressed. A control rule of equal difficulty was learned much more slowly. A programming language withheld from the training text of a 7-billion-parameter model was regained in the same way. Data filtering therefore delays a capability, and the data required to regain it decreases as models improve.

**Sektörel Etki & Anlamı:**
Research alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [http://arxiv.org/abs/2611.24844v1](http://arxiv.org/abs/2611.24844v1)

---

### [[ArXiv] Can Programs Replace LLM Judges? Executable Program Judges for Scalable and Efficient Relevance Labeling](http://arxiv.org/abs/2611.24849v1)
**Öne Çıkanlar:**
  - [ArXiv] Can Programs Replace LLM Judges? Executable Program Judges for Scalable and Efficient Relevance Labeling: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
Large language model (LLM) judges have become a common way to create large-scale relevance judgments for retrieval evaluation. However, each judgment requires a potentially expensive call to a frontier model, and the judgments are hard to interpret and may not be reproducible. In this paper, we ask whether an LLM can write a readable program for each topic that replaces its per-document judgments. To address these issues, we propose ExecJudges, a method for generating fast, inspectable and scalable judges for automatic relevance labeling. Specifically, ExecJudges uses a frontier LLM to turn assessment guidelines into executable programs, which rely only on lexical matching, standard NLP libraries like parsers, and pool statistics. An ExecJudges-L variant also uses examples of human labels if available. We evaluate ExecJudges on seven TREC collections by comparing the produced labels with trained NIST assessors, frontier LLM judges, and recently proposed per-topic classifiers. Our results show that ExecJudges agrees with NIST assessors at the level of the Claude Sonnet 5.5 LLM judges on TREC DL 2019-2021. With a small number of human labels per topic, the ExecJudges-L variant agrees with NIST more than per-topic classifiers with the same labels on all seven collections, and either exceeds the agreement of LLM judges provided the same labels or is within about 0.05 of it in Krippendorff's alpha. The labels rank the official TREC DL runs with Kendall's tau of 0.87 to 0.94, and w

**Sektörel Etki & Anlamı:**
Research alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [http://arxiv.org/abs/2611.24849v1](http://arxiv.org/abs/2611.24849v1)


---

## 🛠️ Araçlar, Modeller ve Açık Kaynak (Tooling, Frameworks & Releases)
### [Google DeepMind Releases Gemini 4 Neon: 1M Context, #1 on AA Coding Agent Index](https://www.marktechpost.com/2026/11/18/google-gemini-4-neon-release/)
**Öne Çıkanlar:**
  - Google DeepMind Releases Gemini 4 Neon: 1M Context, #1 on AA Coding Agent Index: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
Google released Gemini 4 Neon, a 1M-context Gemini 4 model priced at $3/$15 per million tokens. It scores 61 on the AA Intelligence Index and ranks #1 on AA’s Coding Agent Index. The post Google DeepMind Releases Gemini 4 Neon: 1M Context, #1 on AA Coding Agent Index appeared first on MarkTechPost .

**Sektörel Etki & Anlamı:**
LLM Release alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [https://www.marktechpost.com/2026/11/18/google-gemini-4-neon-release/](https://www.marktechpost.com/2026/11/18/google-gemini-4-neon-release/)

---

### [New LoRA Adapter Lifts Qwen3.8 Coding Success From 39% to 65%](https://www.marktechpost.com/2026/11/18/hugging-face-qwen3-8-27b-pi-adapted-lora/)
**Öne Çıkanlar:**
  - New LoRA Adapter Lifts Qwen3.8 Coding Success From 39% to 65%: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
Hugging Face released Qwen3.8-27B-pi-adapted, an Apache-2.0 LoRA adapter trained with reinforcement learning for the pi coding agent. It lifts SWE-bench Pro hard-51 pass@1 from 39.2% to 64.7% and Terminal-Bench 2.1 from 39.5% to 55.8%. The post New LoRA Adapter Lifts Qwen3.8 Coding Success From 39% to 65% appeared first on MarkTechPost .

**Sektörel Etki & Anlamı:**
LLM Release alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [https://www.marktechpost.com/2026/11/18/hugging-face-qwen3-8-27b-pi-adapted-lora/](https://www.marktechpost.com/2026/11/18/hugging-face-qwen3-8-27b-pi-adapted-lora/)

---

### [DaisyRose-27B: Pushing the Frontier of Post-Training Efficiency](https://huggingface.co/blog/RadixArk/daisyrose-27b-pushing-the-frontier-of-post-trainin)
**Öne Çıkanlar:**
  - DaisyRose-27B: Pushing the Frontier of Post-Training Efficiency: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
DaisyRose-27B: Pushing the Frontier of Post-Training Efficiency

**Sektörel Etki & Anlamı:**
LLM Release alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [https://huggingface.co/blog/RadixArk/daisyrose-27b-pushing-the-frontier-of-post-trainin](https://huggingface.co/blog/RadixArk/daisyrose-27b-pushing-the-frontier-of-post-trainin)


---

## 📚 Kaynak Rehberi ve Orijinal Bağlantılar
| # | Başlık | Kaynak | Doğrudan Link |
|---|---|---|---|
| 1 | Google DeepMind Releases Gemini 4 Neon: 1M Context, #1 on AA Coding Agent Index | `www.marktechpost.com` | [İncele](https://www.marktechpost.com/2026/11/18/google-gemini-4-neon-release/) |
| 2 | New LoRA Adapter Lifts Qwen3.8 Coding Success From 39% to 65% | `www.marktechpost.com` | [İncele](https://www.marktechpost.com/2026/11/18/hugging-face-qwen3-8-27b-pi-adapted-lora/) |
| 3 | [ArXiv] General progress substitutes for specific training data in language models | `arxiv.org` | [İncele](http://arxiv.org/abs/2611.24844v1) |
| 4 | DaisyRose-27B: Pushing the Frontier of Post-Training Efficiency | `huggingface.co` | [İncele](https://huggingface.co/blog/RadixArk/daisyrose-27b-pushing-the-frontier-of-post-trainin) |
| 5 | [ArXiv] Can Programs Replace LLM Judges? Executable Program Judges for Scalable and Efficient Relevance Labeling | `arxiv.org` | [İncele](http://arxiv.org/abs/2611.24849v1) |

---
*Bu rapor LangGraph ve AI Multi-Agent StateGraph mimarisi ile her sabah otomatik olarak üretilmektedir.*
