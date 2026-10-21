# 🤖 Yapay Zeka Günlük İstihbarat Bülteni — 2026-10-21

> 📅 **Tarih:** 2026-10-21 | 🌐 **Dil:** Türkçe | ⚡ **Durum:** Otomatik Raporlandı

## ⚡ Yönetici Özeti (TL;DR)
- **Mistral AI Releases Voxtral 3: Speech-to-Text, TTS and a Voice Agent SDK**: Mistral AI released Voxtral 3, a family of 3 transcription models, 1 text-to-speech model and a LiveKit-based voice agent SDK. Voxtral Small Transcribe 3 scores 2.1% AA-WER, ranking #3 on Artificial A
- **Google Cloud Ships llm-d 1.0 With Cache-Aware Routing for TPU and GPU Fleets**: Google, Red Hat and IBM released llm-d 1.0, an open-source Kubernetes-native stack for distributed LLM inference. It adds multi-tenant flow control, zero-downtime upgrades and agent-aware routing acro
- **Google Open-Sources TorchTPU, a Native PyTorch Backend for Cloud TPUs**: Google and Meta open-sourced TorchTPU, a native PyTorch backend for Cloud TPUs. It runs eager by default, compiles through torch.compile and XLA, and replaces PyTorch/XLA for new workloads. The post G

---

## 🔬 Araştırma ve Çığır Açan Gelişmeler (Research & Breakthroughs)
### [[ArXiv] Large Flow Language Models](http://arxiv.org/abs/2610.28559v1)
**Öne Çıkanlar:**
  - Continuous flow language models offer a path to parallel generation with tools for control and acceleration unavailable to discrete diffusion, yet effective techniques for building them at the billion

**Teknik Derinlik & Mimari:**
Continuous flow language models offer a path to parallel generation with tools for control and acceleration unavailable to discrete diffusion, yet effective techniques for building them at the billion-parameter scale remain less established. We present Lafa (Large flow language model), a fast, high-performing flow language model scaled to 8B parameters in a data-efficient manner. Lafa is a blockwise flow model with causal attention on the prefix and bidirectional, asynchronous flow within each block. This design enables efficient training by adapting pretrained autoregressive (AR) models and fast inference via prefix caching and blockwise parallel decoding. We train Lafa at 0.5B, 7B, and 8B scales with fewer than 30B tokens, more efficient than previous diffusion models, and evaluate it on instruction following, reasoning, and coding, where the learned flow matches or surpasses the quality of AR and can be distilled into flow maps for one- and few-step generation. Notably, flow training preserves or even improves pretrained AR capabilities via a multi-token prediction effect, which we leverage in a self-speculative decoding scheme that verifies flow-based drafts autoregressively within a single model. This yields 2.54x the throughput of an AR model at comparable quality, outperforming multi-token prediction and discrete diffusion methods. Our findings show that continuous flows can serve as a scalable foundation for language modeling.

**Sektörel Etki & Anlamı:**
Research kategorisinde önemli bir gelişme.

📎 *Kaynak Bağlantısı:* [http://arxiv.org/abs/2610.28559v1](http://arxiv.org/abs/2610.28559v1)

---

### [[ArXiv] Capable Teacher, Myopic Scorer: Reward-Free Teacher Repair for Agentic On-Policy Distillation](http://arxiv.org/abs/2610.28586v1)
**Öne Çıkanlar:**
  - Agentic on-policy distillation (OPD) trains a student agent on its own trajectories while a teacher scores every token. A natural explanation of where it goes wrong is compounding error: the student's

**Teknik Derinlik & Mimari:**
Agentic on-policy distillation (OPD) trains a student agent on its own trajectories while a teacher scores every token. A natural explanation of where it goes wrong is compounding error: the student's mistakes carry its trajectories beyond the region where the teacher is reliable, so recent methods keep training inside that region, through episode-length curricula, teacher-guided turns, prefix replay, or teacher intervention where the two disagree. We show this explanation is incomplete. From the states where the student departs most from the teacher, the teacher's own takeovers still finish the task, yet the student trained on its token scores keeps running out of turns. We attribute this to the myopia of next-token scoring. The teacher rates each token without seeing where the episode ends, so its scores let through the safe, delaying moves that outcome-based RL would punish with zero reward, a penalty agentic OPD lacks. We call this difference between what the teacher does and what it scores the rollout-scorer gap. We propose Rollout-to-Scorer Distillation (R2S), which repairs the scorer before distillation by mining high-disagreement states from the untrained student, running teacher takeovers from them, keeping the states where enough takeovers pass a reward-free check such as consensus or an LLM judge, and fine-tuning the teacher to give its takeover-informed scores on every assistant token from the divergence turn onward, without the takeover in context. The repaired t

**Sektörel Etki & Anlamı:**
Research kategorisinde önemli bir gelişme.

📎 *Kaynak Bağlantısı:* [http://arxiv.org/abs/2610.28586v1](http://arxiv.org/abs/2610.28586v1)

---

### [[ArXiv] Cache Engineering for Agents](http://arxiv.org/abs/2610.28577v1)
**Öne Çıkanlar:**
  - Large Language Model (LLM) agents can handle increasingly complex tasks, navigating long trajectories of observations and actions. As these trajectories grow, key-value (KV) cache I/O and storage beco

**Teknik Derinlik & Mimari:**
Large Language Model (LLM) agents can handle increasingly complex tasks, navigating long trajectories of observations and actions. As these trajectories grow, key-value (KV) cache I/O and storage become the dominant cost. Trajectories can also exceed the LLM's maximum context length, requiring control over active cache growth. Prior work uses context engineering to reduce cache size by trimming or summarizing history. However, modifying the trajectory prefix invalidates subsequent cached states and triggers costly re-prefilling of retained context. Task accuracy can also suffer when too little context is retained to limit re-prefill costs. We propose cache engineering as a new scheme. It allows agents to directly control their active KV cache without modifying the trajectory or re-prefilling retained context. Specifically, agents can proactively use drop to exclude selected cache from future attention and repos to adjust retained keys' position encodings. We formalize these cache operations and identify history dependence as a serving challenge: identical token sequences can yield different cache states under different cache operation sequences, making prefix matching insufficient for correct cache reuse. Thus, we co-design the AKV serving engine. It provides a stateless interface compatible with existing serving APIs, while internally managing stateful cache reuse, eviction, and restoration. Experiments show that a tool-response rolling-drop cache policy improves average ben

**Sektörel Etki & Anlamı:**
Research kategorisinde önemli bir gelişme.

📎 *Kaynak Bağlantısı:* [http://arxiv.org/abs/2610.28577v1](http://arxiv.org/abs/2610.28577v1)


---

## 🛠️ Araçlar, Modeller ve Açık Kaynak (Tooling, Frameworks & Releases)
### [Mistral AI Releases Voxtral 3: Speech-to-Text, TTS and a Voice Agent SDK](https://www.marktechpost.com/2026/10/20/mistral-voxtral-3-speech-models-voice-agent-sdk/)
**Öne Çıkanlar:**
  - Mistral AI released Voxtral 3, a family of 3 transcription models, 1 text-to-speech model and a LiveKit-based voice agent SDK. Voxtral Small Transcribe 3 scores 2.1% AA-WER, ranking #3 on Artificial A

**Teknik Derinlik & Mimari:**
Mistral AI released Voxtral 3, a family of 3 transcription models, 1 text-to-speech model and a LiveKit-based voice agent SDK. Voxtral Small Transcribe 3 scores 2.1% AA-WER, ranking #3 on Artificial Analysis. The post Mistral AI Releases Voxtral 3: Speech-to-Text, TTS and a Voice Agent SDK appeared first on MarkTechPost .

**Sektörel Etki & Anlamı:**
LLM Release kategorisinde önemli bir gelişme.

📎 *Kaynak Bağlantısı:* [https://www.marktechpost.com/2026/10/20/mistral-voxtral-3-speech-models-voice-agent-sdk/](https://www.marktechpost.com/2026/10/20/mistral-voxtral-3-speech-models-voice-agent-sdk/)

---

### [Google Cloud Ships llm-d 1.0 With Cache-Aware Routing for TPU and GPU Fleets](https://www.marktechpost.com/2026/10/20/llm-d-1-0-open-source-distributed-inference-stack/)
**Öne Çıkanlar:**
  - Google, Red Hat and IBM released llm-d 1.0, an open-source Kubernetes-native stack for distributed LLM inference. It adds multi-tenant flow control, zero-downtime upgrades and agent-aware routing acro

**Teknik Derinlik & Mimari:**
Google, Red Hat and IBM released llm-d 1.0, an open-source Kubernetes-native stack for distributed LLM inference. It adds multi-tenant flow control, zero-downtime upgrades and agent-aware routing across vLLM, SGLang, TPUs and GPUs. The post Google Cloud Ships llm-d 1.0 With Cache-Aware Routing for TPU and GPU Fleets appeared first on MarkTechPost .

**Sektörel Etki & Anlamı:**
Tooling kategorisinde önemli bir gelişme.

📎 *Kaynak Bağlantısı:* [https://www.marktechpost.com/2026/10/20/llm-d-1-0-open-source-distributed-inference-stack/](https://www.marktechpost.com/2026/10/20/llm-d-1-0-open-source-distributed-inference-stack/)

---

### [Google Open-Sources TorchTPU, a Native PyTorch Backend for Cloud TPUs](https://www.marktechpost.com/2026/10/20/google-torchtpu-open-source-native-pytorch-tpu/)
**Öne Çıkanlar:**
  - Google and Meta open-sourced TorchTPU, a native PyTorch backend for Cloud TPUs. It runs eager by default, compiles through torch.compile and XLA, and replaces PyTorch/XLA for new workloads. The post G

**Teknik Derinlik & Mimari:**
Google and Meta open-sourced TorchTPU, a native PyTorch backend for Cloud TPUs. It runs eager by default, compiles through torch.compile and XLA, and replaces PyTorch/XLA for new workloads. The post Google Open-Sources TorchTPU, a Native PyTorch Backend for Cloud TPUs appeared first on MarkTechPost .

**Sektörel Etki & Anlamı:**
Tooling kategorisinde önemli bir gelişme.

📎 *Kaynak Bağlantısı:* [https://www.marktechpost.com/2026/10/20/google-torchtpu-open-source-native-pytorch-tpu/](https://www.marktechpost.com/2026/10/20/google-torchtpu-open-source-native-pytorch-tpu/)

---

### [DeepSeek Open-Sources DeepInfer, the Inference Framework Behind DeepSeek-V4.1-Flash](https://www.marktechpost.com/2026/10/20/deepseek-deepinfer-open-source-inference-framework/)
**Öne Çıkanlar:**
  - DeepSeek has open-sourced DeepInfer, the Apache 2.0 inference framework that serves DeepSeek-V4.1-Flash in production. It targets NVIDIA SM100 GPUs and Huawei Ascend 950 NPUs, and ships offline infere

**Teknik Derinlik & Mimari:**
DeepSeek has open-sourced DeepInfer, the Apache 2.0 inference framework that serves DeepSeek-V4.1-Flash in production. It targets NVIDIA SM100 GPUs and Huawei Ascend 950 NPUs, and ships offline inference only. The post DeepSeek Open-Sources DeepInfer, the Inference Framework Behind DeepSeek-V4.1-Flash appeared first on MarkTechPost .

**Sektörel Etki & Anlamı:**
Tooling kategorisinde önemli bir gelişme.

📎 *Kaynak Bağlantısı:* [https://www.marktechpost.com/2026/10/20/deepseek-deepinfer-open-source-inference-framework/](https://www.marktechpost.com/2026/10/20/deepseek-deepinfer-open-source-inference-framework/)

---

### [ALTK-Evolve: How learned memory tops the τ²-bench leaderboard on customer service tasks without a frontier model](https://huggingface.co/blog/ibm-research/altk-evolve-bc)
**Öne Çıkanlar:**
  - ALTK-Evolve: How learned memory tops the τ²-bench leaderboard on customer service tasks without a frontier model

**Teknik Derinlik & Mimari:**
ALTK-Evolve: How learned memory tops the τ²-bench leaderboard on customer service tasks without a frontier model

**Sektörel Etki & Anlamı:**
Research kategorisinde önemli bir gelişme.

📎 *Kaynak Bağlantısı:* [https://huggingface.co/blog/ibm-research/altk-evolve-bc](https://huggingface.co/blog/ibm-research/altk-evolve-bc)


---

## 📚 Kaynak Rehberi ve Orijinal Bağlantılar
| # | Başlık | Kaynak | Doğrudan Link |
|---|---|---|---|
| 1 | Mistral AI Releases Voxtral 3: Speech-to-Text, TTS and a Voice Agent SDK | `www.marktechpost.com` | [İncele](https://www.marktechpost.com/2026/10/20/mistral-voxtral-3-speech-models-voice-agent-sdk/) |
| 2 | Google Cloud Ships llm-d 1.0 With Cache-Aware Routing for TPU and GPU Fleets | `www.marktechpost.com` | [İncele](https://www.marktechpost.com/2026/10/20/llm-d-1-0-open-source-distributed-inference-stack/) |
| 3 | Google Open-Sources TorchTPU, a Native PyTorch Backend for Cloud TPUs | `www.marktechpost.com` | [İncele](https://www.marktechpost.com/2026/10/20/google-torchtpu-open-source-native-pytorch-tpu/) |
| 4 | DeepSeek Open-Sources DeepInfer, the Inference Framework Behind DeepSeek-V4.1-Flash | `www.marktechpost.com` | [İncele](https://www.marktechpost.com/2026/10/20/deepseek-deepinfer-open-source-inference-framework/) |
| 5 | [ArXiv] Large Flow Language Models | `arxiv.org` | [İncele](http://arxiv.org/abs/2610.28559v1) |
| 6 | ALTK-Evolve: How learned memory tops the τ²-bench leaderboard on customer service tasks without a frontier model | `huggingface.co` | [İncele](https://huggingface.co/blog/ibm-research/altk-evolve-bc) |
| 7 | [ArXiv] Capable Teacher, Myopic Scorer: Reward-Free Teacher Repair for Agentic On-Policy Distillation | `arxiv.org` | [İncele](http://arxiv.org/abs/2610.28586v1) |
| 8 | [ArXiv] Cache Engineering for Agents | `arxiv.org` | [İncele](http://arxiv.org/abs/2610.28577v1) |

---
*Bu rapor LangGraph ve AI Multi-Agent StateGraph mimarisi ile her sabah otomatik olarak üretilmektedir.*
