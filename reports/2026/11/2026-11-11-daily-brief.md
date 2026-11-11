# 🤖 Yapay Zeka Günlük İstihbarat Bülteni — 2026-11-11

> 📅 **Tarih:** 2026-11-11 | 🌐 **Dil:** Türkçe | ⚡ **Durum:** Otomatik Raporlandı

## ⚡ Yönetici Özeti (TL;DR)
- **Anthropic Launches Claude Fable 5.2 and Mythos 5.2: Same Model, Different Safeguards**: Anthropic Launches Claude Fable 5.2 and Mythos 5.2: Same Model, Different Safeguards: Gelişme detayları inceleniyor.
- **MBZUAI’s IFM Releases PAN 2, an Open 29B World Model for Physical AI**: MBZUAI’s IFM Releases PAN 2, an Open 29B World Model for Physical AI: Gelişme detayları inceleniyor.
- **Meta FAIR Releases e-means: An Algorithm Beating k-means in 10x Fewer Epochs**: Meta FAIR Releases e-means: An Algorithm Beating k-means in 10x Fewer Epochs: Gelişme detayları inceleniyor.

---

## 🔬 Araştırma ve Çığır Açan Gelişmeler (Research & Breakthroughs)
### [[ArXiv] AutoScaffold: AI-Guided Scaffolding for Reinforcement Learning of Language Models](http://arxiv.org/abs/2611.14515v1)
**Öne Çıkanlar:**
  - [ArXiv] AutoScaffold: AI-Guided Scaffolding for Reinforcement Learning of Language Models: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
Reinforcement learning with verifiable rewards (RLVR) produces rich training experience, yet outcome rewards reduce each attempt to a single number and leave most of this information unused. Training-time scaffolds, such as strategies or hints added to the prompt during training, offer a natural way to turn this information into guidance, but their design and adaptation are largely left to humans and tailored to specific domains. We introduce AutoScaffold, a unified AI-for-AI framework that turns a student's training experience into adaptive scaffolds, with minimal domain-specific information and no human intervention during training. A frozen teacher periodically examines this experience, diagnoses bottlenecks, and designs scaffolds in two forms: (i) strategies shared across a class of tasks and (ii) hints for individual hard tasks, adjusting the content and amount of support as the student learns. The scaffolds are removed at evaluation. We apply the same framework to ALFWorld, search-based QA, mathematical reasoning, and GPU kernel generation. When evaluated without scaffolds, students trained with AutoScaffold outperform those trained with the corresponding RL baselines in all four domains, with gains of 7.2 points in ALFWorld success and 4.0 points in average QA exact match. On GPU kernel generation, AutoScaffold increases the fraction of tasks with a correct kernel that runs faster than the PyTorch reference by up to 5.0 points. On math, our student surpasses QuestA's r

**Sektörel Etki & Anlamı:**
Research alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [http://arxiv.org/abs/2611.14515v1](http://arxiv.org/abs/2611.14515v1)

---

### [[ArXiv] Contrastive Discovery: Open-Ended Scientific Discovery over Competing Explanations](http://arxiv.org/abs/2611.14514v1)
**Öne Çıkanlar:**
  - [ArXiv] Contrastive Discovery: Open-Ended Scientific Discovery over Competing Explanations: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
LLM agents are increasingly used for open-ended, data-driven scientific discovery, yet most of them evaluate hypotheses pointwise, testing an empirical claim $h$ only against its complement $\neg h$. When evidence rejects $h$, the agent learns that one explanation is unlikely but not which alternative the evidence supports. To recover that alternative, we introduce Contrastive Discovery, which replaces the single hypothesis with a contrast set, a scientific question paired with mutually exclusive and collectively exhaustive competing explanations. Each experiment is scored by how its evidence redistributes belief across the set, and the question is resolved when belief concentrates on one explanation. Because contrast sets change only the unit an agent proposes and scores, an existing agent can use them to re-evaluate evidence it has already collected or to guide its search. Across six domains, $89\%$ of the pointwise candidates with the largest belief shifts are rejections. On the same evidence, contrast sets resolve $73\%$ of these candidates to a specific alternative. When contrast sets guide search, the agent resolves $67\%$ more questions than pointwise surprisal under the same experiment budget. In a blinded study, $38$ human experts chose the same explanation on $78\%$ of resolved questions and on $82\%$ of questions where the pointwise agent rejected its hypothesis and stopped. Together, these results support explicit competing explanations as a way for discovery agen

**Sektörel Etki & Anlamı:**
Research alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [http://arxiv.org/abs/2611.14514v1](http://arxiv.org/abs/2611.14514v1)


---

## 🛠️ Araçlar, Modeller ve Açık Kaynak (Tooling, Frameworks & Releases)
### [Anthropic Launches Claude Fable 5.2 and Mythos 5.2: Same Model, Different Safeguards](https://www.marktechpost.com/2026/11/10/anthropic-claude-fable-5-2-mythos-5-2-release/)
**Öne Çıkanlar:**
  - Anthropic Launches Claude Fable 5.2 and Mythos 5.2: Same Model, Different Safeguards: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
Anthropic released Claude Fable 5.2 and Claude Mythos 5.2, one model with two safeguard levels. Fable 5.2 scores 49.1% on FrontierCode 2.0, costs $8/$40 per million tokens, and ships with a 1M-token context window. The post Anthropic Launches Claude Fable 5.2 and Mythos 5.2: Same Model, Different Safeguards appeared first on MarkTechPost .

**Sektörel Etki & Anlamı:**
LLM Release alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [https://www.marktechpost.com/2026/11/10/anthropic-claude-fable-5-2-mythos-5-2-release/](https://www.marktechpost.com/2026/11/10/anthropic-claude-fable-5-2-mythos-5-2-release/)

---

### [MBZUAI’s IFM Releases PAN 2, an Open 29B World Model for Physical AI](https://www.marktechpost.com/2026/11/10/ifm-pan-2-open-world-model/)
**Öne Çıkanlar:**
  - MBZUAI’s IFM Releases PAN 2, an Open 29B World Model for Physical AI: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
The Institute of Foundation Models at MBZUAI released PAN 2, an Apache 2.0 world model that couples an LLM planner with a 29B diffusion transformer to simulate up to 20 seconds of action outcomes as video. The post MBZUAI&#8217;s IFM Releases PAN 2, an Open 29B World Model for Physical AI appeared first on MarkTechPost .

**Sektörel Etki & Anlamı:**
LLM Release alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [https://www.marktechpost.com/2026/11/10/ifm-pan-2-open-world-model/](https://www.marktechpost.com/2026/11/10/ifm-pan-2-open-world-model/)

---

### [Meta FAIR Releases e-means: An Algorithm Beating k-means in 10x Fewer Epochs](https://www.marktechpost.com/2026/11/10/meta-fair-e-means-k-means-faiss/)
**Öne Çıkanlar:**
  - Meta FAIR Releases e-means: An Algorithm Beating k-means in 10x Fewer Epochs: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
Meta FAIR’s e-means is a mini-batch k-means replacement shipped in FAISS 1.16.0. It reaches Lloyd’s 25-epoch loss in 1.4 to 2.6 epochs, with 10-45x GPU speedups and no extra hyperparameters. The post Meta FAIR Releases e-means: An Algorithm Beating k-means in 10x Fewer Epochs appeared first on MarkTechPost .

**Sektörel Etki & Anlamı:**
Research alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [https://www.marktechpost.com/2026/11/10/meta-fair-e-means-k-means-faiss/](https://www.marktechpost.com/2026/11/10/meta-fair-e-means-k-means-faiss/)

---

### [BotPsy: On-Device Personal Assistant with a Sub-Billion-Parameter Agentic Language Model](https://huggingface.co/blog/qvac/botpsy)
**Öne Çıkanlar:**
  - BotPsy: On-Device Personal Assistant with a Sub-Billion-Parameter Agentic Language Model: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
BotPsy: On-Device Personal Assistant with a Sub-Billion-Parameter Agentic Language Model

**Sektörel Etki & Anlamı:**
Research alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [https://huggingface.co/blog/qvac/botpsy](https://huggingface.co/blog/qvac/botpsy)

---

### [Fish Audio Releases Live 3, a Full-Duplex Voice Model That Reacts in 186 ms](https://www.marktechpost.com/2026/11/10/fish-audio-live-3-full-duplex-voice-model/)
**Öne Çıkanlar:**
  - Fish Audio Releases Live 3, a Full-Duplex Voice Model That Reacts in 186 ms: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
Fish Audio released Live 3, a full-duplex voice model for voice agents. It listens while it speaks, separates “mm-hmm” from real interruptions, and can react in as little as 186 ms. English only at launch The post Fish Audio Releases Live 3, a Full-Duplex Voice Model That Reacts in 186 ms appeared first on MarkTechPost .

**Sektörel Etki & Anlamı:**
LLM Release alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [https://www.marktechpost.com/2026/11/10/fish-audio-live-3-full-duplex-voice-model/](https://www.marktechpost.com/2026/11/10/fish-audio-live-3-full-duplex-voice-model/)

---

### [Zyphra Releases ZONOS3-Mini: Open-Source TTS With 100M Active Parameters](https://www.marktechpost.com/2026/11/10/zyphra-zonos3-mini-open-source-tts/)
**Öne Çıkanlar:**
  - Zyphra Releases ZONOS3-Mini: Open-Source TTS With 100M Active Parameters: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
Zyphra released ZONOS3-Mini, an Apache 2.0 text-to-speech model with 800M total and 100M active parameters. It clones voices, steers delivery word by word and runs in real time in the browser The post Zyphra Releases ZONOS3-Mini: Open-Source TTS With 100M Active Parameters appeared first on MarkTechPost .

**Sektörel Etki & Anlamı:**
LLM Release alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [https://www.marktechpost.com/2026/11/10/zyphra-zonos3-mini-open-source-tts/](https://www.marktechpost.com/2026/11/10/zyphra-zonos3-mini-open-source-tts/)


---

## 📚 Kaynak Rehberi ve Orijinal Bağlantılar
| # | Başlık | Kaynak | Doğrudan Link |
|---|---|---|---|
| 1 | Anthropic Launches Claude Fable 5.2 and Mythos 5.2: Same Model, Different Safeguards | `www.marktechpost.com` | [İncele](https://www.marktechpost.com/2026/11/10/anthropic-claude-fable-5-2-mythos-5-2-release/) |
| 2 | MBZUAI’s IFM Releases PAN 2, an Open 29B World Model for Physical AI | `www.marktechpost.com` | [İncele](https://www.marktechpost.com/2026/11/10/ifm-pan-2-open-world-model/) |
| 3 | Meta FAIR Releases e-means: An Algorithm Beating k-means in 10x Fewer Epochs | `www.marktechpost.com` | [İncele](https://www.marktechpost.com/2026/11/10/meta-fair-e-means-k-means-faiss/) |
| 4 | [ArXiv] AutoScaffold: AI-Guided Scaffolding for Reinforcement Learning of Language Models | `arxiv.org` | [İncele](http://arxiv.org/abs/2611.14515v1) |
| 5 | BotPsy: On-Device Personal Assistant with a Sub-Billion-Parameter Agentic Language Model | `huggingface.co` | [İncele](https://huggingface.co/blog/qvac/botpsy) |
| 6 | Fish Audio Releases Live 3, a Full-Duplex Voice Model That Reacts in 186 ms | `www.marktechpost.com` | [İncele](https://www.marktechpost.com/2026/11/10/fish-audio-live-3-full-duplex-voice-model/) |
| 7 | Zyphra Releases ZONOS3-Mini: Open-Source TTS With 100M Active Parameters | `www.marktechpost.com` | [İncele](https://www.marktechpost.com/2026/11/10/zyphra-zonos3-mini-open-source-tts/) |
| 8 | [ArXiv] Contrastive Discovery: Open-Ended Scientific Discovery over Competing Explanations | `arxiv.org` | [İncele](http://arxiv.org/abs/2611.14514v1) |

---
*Bu rapor LangGraph ve AI Multi-Agent StateGraph mimarisi ile her sabah otomatik olarak üretilmektedir.*
