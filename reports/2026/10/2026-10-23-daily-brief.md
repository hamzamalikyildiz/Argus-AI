# 🤖 Yapay Zeka Günlük İstihbarat Bülteni — 2026-10-23

> 📅 **Tarih:** 2026-10-23 | 🌐 **Dil:** Türkçe | ⚡ **Durum:** Otomatik Raporlandı

## ⚡ Yönetici Özeti (TL;DR)
- **[ArXiv] Low-Bit N-Gram Embeddings for Language Models**: [ArXiv] Low-Bit N-Gram Embeddings for Language Models: Gelişme detayları inceleniyor.
- **[ArXiv] Causal Chain of Thought: Mitigating Attention Leakage via Context Isolation**: [ArXiv] Causal Chain of Thought: Mitigating Attention Leakage via Context Isolation: Gelişme detayları inceleniyor.
- **[ArXiv] Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success**: [ArXiv] Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success: Gelişme detayları inceleniyor.

---

## 🔬 Araştırma ve Çığır Açan Gelişmeler (Research & Breakthroughs)
### [[ArXiv] Low-Bit N-Gram Embeddings for Language Models](http://arxiv.org/abs/2610.31646v1)
**Öne Çıkanlar:**
  - [ArXiv] Low-Bit N-Gram Embeddings for Language Models: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
Many recent open-weight language models use n-gram embedding tables to improve performance. These tables store learned representations of short token sequences, such as pairs or triples of consecutive tokens, which the model retrieves during processing. However, they can require substantial memory: DeepSeek-V4.1-Flash, for example, allocates 196 billion parameters to its Engram n-gram memory. We therefore investigate whether this memory cost can be reduced while preserving the performance improvement that the tables provide. We propose storing n-gram embeddings at low precision and systematically investigate different quantization methods and bit allocations across tables. Across nanochat-, Llama-, and GPT-2-family models trained from scratch, four-bit tables save approximately 75% of table memory while preserving more than 99% of the validation-loss improvement from adding the tables. Using fewer bits leads to a larger drop in performance, although we find that a short fine-tuning phase recovers a significant part of this loss. In addition, reinvesting the saved memory in larger tables can improve performance beyond that of the original full-precision tables while still using less memory. These table memory savings also extend to large existing models: on DeepSeek-V4.1-Flash and Qwen3.8-Flash-Next, low-bit tables save 47-55% of table memory, with perplexity increases of less than 1.2% and largely preserved downstream task performance. These findings establish low-bit precisi

**Sektörel Etki & Anlamı:**
Research alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [http://arxiv.org/abs/2610.31646v1](http://arxiv.org/abs/2610.31646v1)

---

### [[ArXiv] Causal Chain of Thought: Mitigating Attention Leakage via Context Isolation](http://arxiv.org/abs/2610.31639v1)
**Öne Çıkanlar:**
  - [ArXiv] Causal Chain of Thought: Mitigating Attention Leakage via Context Isolation: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
Chain-of-thought (CoT) prompting elicits step-by-step rationales that appear to explain model predictions, but there is no guarantee these steps causally drive the final answer. In standard autoregressive generation, dense attention allows each reasoning step to attend to the full context, enabling the model to derive answers through direct lookup while generating plausible-sounding but post-hoc justifications. We introduce CausalCoT, an inference framework that enforces causal transparency by decomposing problems into a directed acyclic graph of atomic sub-questions, evaluating each node in an isolated context containing only its direct causal parents. This Markovian structure removes attention pathways to non-parent content, making downstream predictions sensitive to local reasoning rather than global context leakage. Across a diverse suite of reasoning benchmarks, CausalCoT preserves competitive predictive performance while improving explanation faithfulness, increasing causal sensitivity of intermediate reasoning steps by an average of 12 and up to 21 percentage points over the strongest baseline. The structured dependency graph additionally enables test-time interventions in which local corrections propagate predictably through downstream reasoning.

**Sektörel Etki & Anlamı:**
Research alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [http://arxiv.org/abs/2610.31639v1](http://arxiv.org/abs/2610.31639v1)

---

### [[ArXiv] Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success](http://arxiv.org/abs/2610.31670v1)
**Öne Çıkanlar:**
  - [ArXiv] Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
Robotic foundation models are typically evaluated through costly closed-loop rollouts, which motivates cheap offline proxies for model capability. The Platonic Representation Hypothesis (PRH) suggests that as representations improve, different modalities such as vision and language converge toward a shared statistical model of reality. We ask whether motion trajectories form another such modality: as embodied models become more capable, should their sensory representations converge toward the structure of physical motion? To examine this, we propose Sensorimotor Alignment ($S^2$), a training-free offline metric that measures how well a model's sensory representation aligns with the geometry of physical motion. We find that $S^2$ correlates positively with downstream robot task success across embodied model families, making it a low-cost offline proxy for prioritizing models before closed-loop evaluation. $S^2$ can also identify promising vision-language model (VLM) backbones even before costly fine-tuning into vision-language-action models (VLAs). Beyond this correlation, $S^2$ offers representation-level explanations for phenomena observed in VLAs and world action models (WAMs). With $S^2$, we extend PRH to embodied models and make sensorimotor alignment empirically measurable, offering insight into why an embodied model succeeds beyond its closed-loop success rate.

**Sektörel Etki & Anlamı:**
Research alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [http://arxiv.org/abs/2610.31670v1](http://arxiv.org/abs/2610.31670v1)

---

### [[ArXiv] Reliable AI-Assisted Decisions via Selective Auditing](http://arxiv.org/abs/2610.31662v1)
**Öne Çıkanlar:**
  - [ArXiv] Reliable AI-Assisted Decisions via Selective Auditing: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
We consider online monitoring of an AI system that produces a sequence of decisions. At each round, the system outputs a proposed decision together with a confidence score estimating the trustworthiness of the decision. The decision and confidence score need not be produced by the same model: for example, one agent may propose a decision, while a separate verifier agent evaluates it and outputs a correctness or safety score. Based on this information, we must decide whether to accept the AI decision automatically or consult an expert, such as a human auditor, who reviews the proposal and either accepts or corrects it. We formulate this task as an online constrained optimization problem in which the goal is to minimize the frequency of expert auditing while guaranteeing that the fraction of AI errors that go unaudited stays below a user-defined threshold. We derive a family of algorithms with provable error-control guarantees with no assumptions, including a method that is optimally efficient: it asymptotically attains the best achievable auditing rate for both adversarial and i.i.d. data streams. Experiments on screening harmful requests to large language models, qualitative text annotation, and data labeling show that our methods achieve valid error control in practice while substantially reducing the need for human auditing compared to baselines.

**Sektörel Etki & Anlamı:**
Research alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [http://arxiv.org/abs/2610.31662v1](http://arxiv.org/abs/2610.31662v1)

---

### [[ArXiv] SpectralCanary: Embarrassingly Simple Low-Frequency Traces for T2I Dataset-Use Auditing](http://arxiv.org/abs/2610.31659v1)
**Öne Çıkanlar:**
  - [ArXiv] SpectralCanary: Embarrassingly Simple Low-Frequency Traces for T2I Dataset-Use Auditing: Gelişme detayları inceleniyor.
  - Detaylı teknik metin için kaynak bağlantısına başvurunuz.

**Teknik Derinlik & Mimari:**
Auditing whether a text-to-image (T2I) model was fine-tuned on a particular image collection is difficult: a model can absorb collection-level visual characteristics without reproducing training images. Proactive dataset-use auditing plants a shared signal in a dataset before release, then later checks whether that signal appears in a suspect model's generated outputs. Existing approaches often trade off verifiability, fidelity, robustness, and deployability. We introduce $\textbf{SpectralCanary}$, which uses a smooth low-pass mask to blend a fixed canary image into every collection image while leaving captions unchanged and requiring neither auxiliary generation nor per-image optimization. A lightweight verifier detects the transferred signal in suspect-model outputs. Across eight tests on the Pokemon dataset and three realistic data transformations, spanning two architectures families, SpectralCanary achieves the highest average per-generation TPR@$1\%$ FPR ($91.1\%$) and fixed threshold model-level accuracy using 30 generations ($94.8\%$) among the evaluated methods. Across five datasets spanning artistic, medical, satellite, and fashion domains with SD3.5, SpectralCanary averages $92.4\%$ per-generation TPR@$1\%$ FPR while preserving the released images (SSIM $0.989$, LPIPS $0.022$) with a near-zero mean change FID (mean $Δ$FID $0.05$) across datasets. Matched-energy ablations on Pokemon and ROCOv2 support our design choice, low-frequency placement transfers more reliably

**Sektörel Etki & Anlamı:**
Research alanında yapay zeka ekosistemi için dikkate değer bir gelişme.

📎 *Kaynak Bağlantısı:* [http://arxiv.org/abs/2610.31659v1](http://arxiv.org/abs/2610.31659v1)


---

## 🛠️ Araçlar, Modeller ve Açık Kaynak (Tooling, Frameworks & Releases)
_Bugün öne çıkan araç/model sürümü bulunmamaktadır._

---

## 📚 Kaynak Rehberi ve Orijinal Bağlantılar
| # | Başlık | Kaynak | Doğrudan Link |
|---|---|---|---|
| 1 | [ArXiv] Low-Bit N-Gram Embeddings for Language Models | `arxiv.org` | [İncele](http://arxiv.org/abs/2610.31646v1) |
| 2 | [ArXiv] Causal Chain of Thought: Mitigating Attention Leakage via Context Isolation | `arxiv.org` | [İncele](http://arxiv.org/abs/2610.31639v1) |
| 3 | [ArXiv] Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success | `arxiv.org` | [İncele](http://arxiv.org/abs/2610.31670v1) |
| 4 | [ArXiv] Reliable AI-Assisted Decisions via Selective Auditing | `arxiv.org` | [İncele](http://arxiv.org/abs/2610.31662v1) |
| 5 | [ArXiv] SpectralCanary: Embarrassingly Simple Low-Frequency Traces for T2I Dataset-Use Auditing | `arxiv.org` | [İncele](http://arxiv.org/abs/2610.31659v1) |

---
*Bu rapor LangGraph ve AI Multi-Agent StateGraph mimarisi ile her sabah otomatik olarak üretilmektedir.*
